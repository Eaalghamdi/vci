TBNAME_PROJECTS = 'projects'
TBNAME_COLORFULNESS = 'colorfulness'
TBNAME_EDGEDETECTION = 'edgedetection'
TBNAME_OBJECTDETECTION = 'objectdetection'
TBNAME_STRUCTSIMILARITY = 'structuralsimilarity'
TBNAME_COMPRESSION = 'compression'
TBNAME_FACEDTECTION = 'facedetection'
TBNAME_MOTION = 'motion'
TBNAME_SALIENCY = 'saliency'

PARAMS_PROJECTS = {
    'projecttitle': 'ProjectTitle',
    'videotitle': 'VideoTitle',
    'videopath': 'VideoPath'
}

PARAMS_COLORFULNESS = {
    'imgname': 'imgname',
    'imgcolor': 'imgcolor',
    'meancolor': 'meancolor',
    'stdcolor': 'stdcolor',
    'meanadj': 'meanadj',
    'stdadj': 'stdadj',
    'meanadjabs': 'meanadjabs',
    'stdadjabs': 'stdadjabs'
}

PARAMS_EDGEDETECTION = {
    'imgname': 'imgname',
    'meanval': 'meanval',
    'stdval': 'stdval',
    'meanadjabs': 'meanadjabs',
    'stdadjabs': 'stdadjabs'
}

PARAMS_OBJECTDETECTION = {
    'imgname': 'imgname',
    'classindex': 'classindex',
    'confidence': 'confidence',
    'bbox': 'bbox'
}

PARAMS_STRUCTSIMILARITY = {
    'imganame': 'imganame',
    'imgbname': 'imgbname',
    'mse': 'mse',
    'ssim': 'ssim'
}

PARAMS_COMPRESSION = {
    'filename': 'filename',
    'cnvformat': 'cnvformat',
    'sizebytprev': 'sizebytprev',
    'sizebytnew': 'sizebytnew',
}

PARAMS_FACEDTECTION = {
    'filename': 'filename',
    'numfaces': 'numfaces',
}

PARAMS_MOTION = {
    'videoname': 'videoname',
    'numberofmovingobjects': 'numberofmovingobjects',
    'movingdurationms': 'movingdurationms',
    'ratioofmovingobjectsns': 'ratioofmovingobjectsns',
    'ratioofmovingobjectsnm': 'ratioofmovingobjectsnm',
    'movingdurtiondifferencemean': 'movingdurtiondifferencemean',
    'movingdurtiondifferencevaraince': 'movingdurtiondifferencevaraince',
    'movingdurtiondifferencesd': 'movingdurtiondifferencesd',
    'ratioofmovingdurtionts': 'ratioofmovingdurtionts',
    'ratioofmovingdurtiontm': 'ratioofmovingdurtiontm',
    'satrtendtimes': 'satrtendtimes',
}

PARAMS_SALIENCY = {
    'filename': 'filename',
    'mean': 'mean',
    'std': 'std'
}


def value_gen(length):
    if length == 1:
        return ('?')
    elif length == 2:
        return ('?', '?')
    elif length == 3:
        return ('?', '?', '?')
    elif length == 4:
        return ('?', '?', '?', '?')
    elif length == 5:
        return ('?', '?', '?', '?', '?')
    elif length == 6:
        return ('?', '?', '?', '?', '?', '?')
    elif length == 7:
        return ('?', '?', '?', '?', '?', '?', '?')
    elif length == 8:
        return ('?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 9:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 10:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 11:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 12:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 13:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 14:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 15:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 16:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 17:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 18:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 19:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
    elif length == 20:
        return ('?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?')
