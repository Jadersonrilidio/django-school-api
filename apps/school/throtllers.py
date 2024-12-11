from rest_framework import throttling

class EnrollmentAnonRateThrottle(throttling.AnonRateThrottle):
    rate = '5/day'