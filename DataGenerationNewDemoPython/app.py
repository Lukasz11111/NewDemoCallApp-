import tornado.ioloop
import tornado.web
import GenData

global routs

def make_app():
    global routs
    routs=[
        (r"/IdentityCompanyName", GenData.IdentityCompanyName),
        (r"/IdentityPerson", GenData.IdentityPerson),
    ]
    return tornado.web.Application(routs)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        result=''
        for x,v in routs:
            result=result+f'<br/><a href={x}>{x}<a>'
        self.write(str(result) )

class GetHandler(tornado.web.RequestHandler):
    def get(self):
        key = self.get_argument('key', None)
        response = {'key': key}
        self.write(response)

if __name__ == "__main__":

    app = make_app()

    app.listen(7000)

    tornado.ioloop.IOLoop.current().start()
