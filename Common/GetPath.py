import os
current_dir = os.getcwd().split("\\")[-1]


def second_path(dir='Config', file=''):
    '''

    :param dir:
    :param file:
    :return:
    '''
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),dir,file)
    file_path = base_dir.replace("\\","/")
    return file_path

def third_path(root='',dir='',file=''):
    '''

    :param root:
    :param dir:
    :param file:
    :return:
    '''
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),root,dir,file)
    file_path = base_dir.replace("\\","/")
    return file_path

