import os, json
import geopandas as gpd

def init_api_token(USER_ID,USER_SECRET):
    # inspiré de https://www.kaggle.com/paultimothymooney/exploring-the-kaggle-api
    import os,json
    KAGGLE_CONFIG_DIR = os.path.join(os.path.expandvars('$HOME'), '.kaggle')
    os.makedirs(KAGGLE_CONFIG_DIR, exist_ok = True)
    with open(os.path.join(KAGGLE_CONFIG_DIR, 'kaggle.json'), 'w') as f:
        json.dump({'username': USER_ID, 'key': USER_SECRET}, f)
        os.chmod( "{}/kaggle.json".format( KAGGLE_CONFIG_DIR),600 )

class Dataset:
    # voir: https://github.com/Kaggle/kaggle-api/
    """
    Get data using kaggle api
    """
    def __init__(self,user,dataset):
        """
        Get dataset of user
        """
        # todo: check if it fails
        # todo: use python functions, not cli
        self.user=user
        self.dataset=dataset
        self.working="/kaggle/working"

    def load(self):
        os.system("kaggle datasets download --unzip -p {} {}/{} ".format(self.dir(),self.user,self.dataset) )
    def dir(self):
       return "{}/{}-{}".format(self.working,self.user, self.dataset)


    def ls(self):
        """
        List available files in this dataset
        """
        return os.listdir(self.dir())

    def shapefile(self):
        """
        return shapefile as geodataframe
        """
        # todo: handle error
        matching = [s for s in self.ls() if ".shp" in s]
        return gpd.read_file("{}/{}".format(self.dir(),matching[0]))
