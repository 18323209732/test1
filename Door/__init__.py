from Door.news.info_st import info_news

all_class = [info_news]

all_dirs = ['AddCategory', 'AddProduct', 'attribute', 'content', 'news', 'productCategory']

class_case = (('manage_productCategory', 'test_add_category'), ('info_news', 'test_all_news'), ('info_news', 'test_noclass_news'), ('info_news', 'test_search_news'), ('info_news', 'test_screen_news'), ('info_news', 'test_turnpage_news'), ('info_news', 'test_theadsort_news'), ('info_news', 'test_dragsort_news'), ('info_news', 'test_edit_news'), ('info_news', 'test_browse_news'), ('info_news', 'test_updatetransfer_news'), ('info_news', 'test_updatepcview_news'), ('info_news', 'test_hide_news'), ('info_news', 'test_copy_news'), ('info_news', 'test_top_news'), ('info_news', 'test_recommend_news'), ('info_news', 'test_savetags_news'), ('info_news', 'test_delete_news'), ('info_news', 'test_transfer_news'), ('info_news', 'test_pcview_news'), ('info_news', 'test_hidepcview_news'), ('info_news', 'test_batchdelete_news'), ('info_news', 'test_batchrecommend_news'), ('info_news', 'test_cancelrecommend_news'), ('info_news', 'test_canceltop_news'), ('info_news', 'test_batchcancel_news'), ('info_news', 'test_customsort_news'))

fail_error = (('manage_productCategory', 'test_add_category'), ('info_news', 'test_hide_news'), ('info_news', 'test_copy_news'))