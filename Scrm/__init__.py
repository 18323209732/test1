from Scrm.product.managess_st import managess_product
from Scrm.product.manage_st import manage_product

all_class = [managess_product, manage_product]

all_dirs = ['product']

class_case = [('manage_product', 'test_product_getlist'), ('manage_product', 'test_product33_getlist'), ('managess_product', 'test_product333_getlist'), ('manage_product', 'test_product33_getlist22')]

fail_error = [('manage_product', 'test_product_getlist'), ('manage_product', 'test_product33_getlist'), ('managess_product', 'test_product333_getlist'), ('manage_product', 'test_product33_getlist22')]