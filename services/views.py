from threading import Timer, Thread

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_imu_config(True, True, True)
default_orient = None
threshold = 80
last_orients = None

def get_mean_orientation():
    a = list()
    for i in range(10):
        a.append(sense.get_orientation())
    l1 = [e["yaw"] for e in a]
    l2 = [e["pitch"] for e in a]
    l3 = [e["roll"] for e in a]
    l1.sort()
    l2.sort()
    l3.sort()
    r = dict()
    r["yaw"] = l1[5]
    r["pitch"] = l2[5]
    r["roll"] = l3[5]
    return r


class RaspViewSet(viewsets.GenericViewSet):

    #sense = SenseHat()
    #sense.set_imu_config(False, True, False)

    def get_sense(self):
        global sense
        return sense

    def mean_orient(self, orients):
        m = dict()
        m["yaw"] = 0
        m["pitch"] = 0
        m["roll"] = 0
        for ori in orients:
            for k in ori:
                m[k] += ori[k]
        for k in m:
            m[k] = m[k]/len(orients)
        return m

    def get_mean_orientation(self):
        l = list()
        for i in range(5):
            orient = self.get_sense().get_orientation_degrees()
            print(orient)
            l.append(orient)
            time.sleep(1)
        m = self.mean_orient(l)
        return m

    def check_fall_roll(self, ore):
        if 80 < ore["roll"] and ore["roll"] < 300:
            return True
        if 0 <= ore["roll"] and ore["roll"] <= 80:
            return False
        if 280 <= ore["roll"] and ore["roll"] <= 360:
            return False
        return True

    def check_fall_pitch(self, ore):
        #310 y 70
        if 0 <= ore["pitch"] and ore["pitch"] <= 70:
            return False
        if 310 <= ore["pitch"] and ore["pitch"] <= 360:
            return False
        return True

    @list_route(methods=['get'])
    def isFall(self, request):
        ore = sense.get_orientation()
        fall = self.check_fall_pitch(ore) or self.check_fall_roll(ore)
        ore["fall"] = fall
        if fall:
            sense.show_letter("X",text_colour=[255,0,0])
        else:
            sense.clear()
        return Response(ore)



