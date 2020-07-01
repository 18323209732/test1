from Door.attribute.add_st import add_attribute
from Door.classification.manage_st import manage_classification
from Door.classify.manage_st import manage_classify

all_class = [add_attribute, manage_classification, manage_classify]

all_dirs = ['attribute', 'classification', 'classify']

class_case = (('manage_classification', 'test_edit_classification'), ('add_attribute', 'test_attribute_list'), ('manage_classification', 'test_see_classification'), ('manage_classification', 'test_classify_add'), ('manage_classification', 'test_classify_update'), ('add_attribute', 'test_add_attribute'), ('manage_classification', 'test_hide_classify'), ('manage_classification', 'test_display_classify'), ('manage_classify', 'test_classify_manage'), ('manage_classify', 'test_add_classify'), ('manage_classify', 'test_edit_classify'), ('manage_classify', 'test_see_classify'), ('add_attribute', 'test_attribute_copy'), ('add_attribute', 'test_attribute_delete'), ('add_attribute', 'test_edit_attribute'), ('add_attribute', 'test_list_screen'), ('manage_classify', 'test_add_classify_picture'))

fail_error = (('manage_classification', 'test_edit_classification'), ('manage_classification', 'test_classify_add'), ('manage_classify', 'test_see_classify'), ('add_attribute', 'test_attribute_copy'), ('manage_classify', 'test_add_classify_picture'))