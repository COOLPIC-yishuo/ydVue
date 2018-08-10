import math
def getpages(total,page,url):
    items = 3
    str1 = '''
         <a href="%s?page=0">首页</a>
        ''' % (url)

    up = page - 1 if page - 1 > 0 else 0
    str1 += '''
             <a href="%s?page=%s">上一页</a>
            ''' % (url, up)
    next = page + 1 if page + 1 < total else page

    before = page if page < math.floor(items / 2) else math.floor(items / 2)
    for item in range(before, 0, -1):
        num = page - item
        if num == page:
            str1 += '''
                      <a href="%s?page=%s" style="color:red">%s</a>
                ''' % (url, num, num + 1)
        else:
            str1 += '''
                  <a href="%s?page=%s">%s</a>
            ''' % (url, num, num + 1)
    after = items - before
    for item in range(after):
        num = page + item
        if (num < total):
            if num == page:
                str1 += '''
                           <a href="%s?page=%s" style="color:red">%s</a>
                     ''' % (url, num, num + 1)
            else:
                str1 += '''
                          <a href="%s?page=%s">%s</a>
                    ''' % (url, num, num + 1)
    str1 += '''
                 <a href="%s?page=%s">下一页</a>
                ''' % (url, next)
    str1 += '''
                 <a href="%s?page=%s">尾页</a>
                ''' % (url, total - 1)
    return str1