import tornado.ioloop
import tornado.web
import GenData

global routs

def make_app():
    global routs
    routs=[
        (r"/IdentityCompanyName", GenData.IdentityCompanyName),
        (r"/IdentityPerson", GenData.IdentityPerson),
        (r"/IdentityPersonAddress", GenData.IdentityPersonAddress),
        (r"/NameCategories", GenData.NameCategories),
        (r"/TriviaSearch", GenData.TriviaSearch),
        (r"/BarcodeEncodeTypes", GenData.BarcodeEncodeTypes),
        (r"/CarcodeDecodeTypes", GenData.CarcodeDecodeTypes),
        (r"/QrcodeBusinessCard", GenData.QrcodeBusinessCard),
        (r"/QrcodeSkype", GenData.QrcodeSkype),
        (r"/QrcodeSms", GenData.QrcodeSms),
        (r"/QrcodeUrl", GenData.QrcodeUrl),
        (r"/QrcodeRaw", GenData.QrcodeRaw),
        (r"/ForgettingRegressionLists", GenData.ForgettingRegressionLists),
        (r"/DataRecession", GenData.DataRecession),
        (r"/SharingInputs", GenData.SharingInputs),
        (r"/SegregationOfStaticFiles", GenData.SegregationOfStaticFiles),
        (r"/TotalQuestionTime", GenData.TotalQuestionTime),
        (r"/InternalMemoryEvaluation", GenData.InternalMemoryEvaluation),
        (r"/CollectionOfPrefallState", GenData.CollectionOfPrefallState),
        (r"/AddingNewThreads", GenData.AddingNewThreads),
        (r"/TurningOffUnnecessaryResources", GenData.TurningOffUnnecessaryResources),
        (r"/CountingBreaks", GenData.CountingBreaks),
        (r"/SendingStates", GenData.SendingStates),
        (r"/ShowAllPreliminaryPossibilities", GenData.ShowAllPreliminaryPossibilities),
        (r"/ReadDataTransformationLogs", GenData.ReadDataTransformationLogs),
        (r"/DatabaseBackupOfAllFirstOccurrences", GenData.DatabaseBackupOfAllFirstOccurrences),
        (r"/StateStates", GenData.StateStates),
        (r"/DetermineTheVitalityOfTheImages", GenData.DetermineTheVitalityOfTheImages),
        (r"/EstimateWeightedMean", GenData.EstimateWeightedMean),
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
