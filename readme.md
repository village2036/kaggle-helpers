# Python utilities for kaggle notebook

    # install library
    ! pip3 install git+https://github.com/village2036/kaggle-utilities.git

    # initialize private api token
    from village2036.kaggle_utils import init_api_token
    init_api_token('username','api_token')  # do not publish this line

    # Import shapefile from a dataset
    from village.kaggle_utils import Dataset
    vpd=Dataset("rngadam","vdq-voies-publiques")
    data=vpd.shapefile()
