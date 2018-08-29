from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

ads = ["IT教育哪家强","你好他好我也好"]
goods = ["该发工资了"]
class AdvertisMiddleware(MiddlewareMixin):

    def process_request(self,req):
        path = req.path
        if path == "/t06/test":
            leads = ["111.198.24.66"]
            # print(req.META.get("REMOTE_ADDR"))
            ip = req.META.get("REMOTE_ADDR")
            if ip in leads:
                return render(req,"advs.html",{"ads":goods})
            else:
                return render(req,"advs.html",{"ads":ads})
        else:
            pass