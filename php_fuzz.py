import re

results = ""
new_results = ""


logo = """                                                                                                
	 ____                   __    __                                                        
	/ ___|  _   _    ___   |  |  |  |  __ __                                                
	\___ \ | | | | /  _  \ |  |——|  | / __` |                                               
	 ___) || |_| ||  (_)  ||  |——|  || (_ ) |_                                              
	|____/  \__,_| \ ___ / |__|  |__| \__,__|_\                                             
                                                                                -- PHP_fuzz     
                                                                                                
                                                                                -- By 414a      

"""

dic = '''
phpcredits(),getenv(),get_defined_vars(),array_rand(),array_reverse(),array_flip(),current(),var_dump(),session_id(),
file_get_contents(),readfile(),highlight_file(),getcwd(),scandir(),phpinfo(),apache_request_headers(),echo(),print_r(),
die(),system(),apache_response_headers(),apache_setenv(),getallheaders(),virtual(),apache_child_terminate(),apache_get_modules(),
apache_get_version(),apache_getenv(),apache_lookup_uri(),apache_note(),chdir(),chroot(),closedir(),dir(),opendir(),readdir(),
rewinddir(),call_user_func_array(),call_user_func(),create_function(),forward_static_call_array(),forward_static_call(),
func_get_arg(),func_get_args(),func_num_args(),function_exists(),get_defined_functions(),register_shutdown_function(),
register_tick_function(),unregister_tick_function(),connection_aborted(),connection_status(),constant(),define(),defined(),
eval(),exit(),get_browser(),__halt_compiler(),highlight_string(),hrtime(),ignore_user_abort(),pack(),php_strip_whitespace(),
show_source(),sleep(),sys_getloadavg(),time_nanosleep(),time_sleep_until(),uniqid(),unpack(),usleep(),scandir(),localeconv(),
pos(),array_flip(),scandir(),array_reverse(),array_rand(),next(),show_source(),file_get_contents(),highlight_file(),
array_​change_​key_​case(),array_chunk(),array_​column(),array_​combine(),array_​count_​values(),array_​diff_​assoc(),array_​diff_​key(),
array_​diff_​uassoc(),array_​diff_​ukey(),array_​diff(),array_​fill_​keys(),array_​fill(),array_​filter(),array_​flip(),array_​intersect_​assoc(),
array_​intersect_​key(),array_​intersect_​uassoc(),array_​intersect_​ukey(),array_​intersect(),array_​is_​list(),array_​key_​exists(),array_​key_​first(),
array_​key_​last(),array_​keys(),array_​map(),array_​merge_​recursive(),array_​merge(),array_​multisort(),array_​pad(),array_​pop(),array_​product(),
array_​push(),array_​rand(),array_​reduce(),array_​replace_​recursive(),array_​replace(),array_​reverse(),array_​search(),array_​shift(),array_​slice(),
array_​splice(),array_​sum(),array_​udiff_​assoc(),array_​udiff_​uassoc(),array_​udiff(),array_​uintersect_​assoc(),array_​uintersect_​uassoc(),
array_​uintersect(),array_​unique(),array_​unshift(),array_​values(),array_​walk_​recursive(),array_​walk(),array(),arsort(),asort(),compact(),
count(),current(),end(),extract(),in_​array(),key_​exists(),key(),krsort(),ksort(),list(),natcasesort(),natsort(),next(),pos(),prev(),
range(),reset(),rsort(),shuffle(),sizeof(),sort(),uasort(),uksort(),usort(),each()
'''

print("\033[0;31;40m" + logo + "\033[0m")
print("use：")
print("输入被过滤函数：o|v|b|print|var|time|file|sqrt|path|dir|exp|pi|an|na|en|ex|et|na|dec|true|false")
print("输入分隔符(直接回车默认为空格)：|")
print("\n")
dic = dic.split(',')
str_filter = input("输入被过滤函数：").lower()
separate = input("输入分隔符(直接回车默认为空格)：")
if separate == "":
    separate = " "
str_filter = str_filter.split(separate)
k = 0
for i in range(0,len(str_filter)):
    
    for j in range(0,len(dic)):
        
        if str_filter[i] not in dic[j]:
            k += 1
        else:
            results += str(dic[j]) + ","
for i in dic:
    if i not in results:
        new_results += str(i)+ ","
new_results = new_results.split(',')
# print(new_results)
for i in new_results:
   print(i.replace("\u200b","").replace("\n",""))

