from userservice.utils.resource import Resource
class Ping(Resource):

    def get(self):
        """
           This method is used to fetch csr details
        """

        return {"success": True}
