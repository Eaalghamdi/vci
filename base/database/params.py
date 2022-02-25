TBNAME_PROJECTS = 'projects'
TBNAME_COLORFULNESS = 'colorfulness'
TBNAME_EDGEDETECTION = 'edgedetection'
TBNAME_OBJECTDETECTION = 'objectdetection'
TBNAME_STRUCTSIMILARITY = 'structuralsimilarity'

PARAMS_PROJECTS = {
    'projecttitle': 'ProjectTitle',
    'videotitle': 'VideoTitle',
    'videopath': 'VideoPath'
}

PARAMS_COLORFULNESS = {
    'imgcolor': 'imgcolor',
    'meancolor': 'meancolor',
    'stdcolor': 'stdcolor',
    'meanadj': 'meanadj',
    'stdadj': 'stdadj',
    'meanadjabs': 'meanadjabs',
    'stdadjabs': 'stdadjabs'
}

PARAMS_EDGEDETECTION = {
    'meanval': 'meanval',
    'stdval': 'stdval',
    'meanadjabs': 'meanadjabs',
    'stdadjabs': 'stdadjabs'
}

PARAMS_OBJECTDETECTION = {
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
