##### 个人Python学习私房菜
> - Python 3.6.2
> - Sublime Text 3

##### Sublime Text 3配置Python开发环境
1. 使用 [Ctrl + `](或View > Show Console menu) 打开Sublime Text控制台，将下面的Python代码粘贴到控制台里:
> import urllib.request,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
2. 按下Ctrl+Shift+P调出命令面板，输入install 调出 Install Package 选项并回车。
3. 在列表中选中要安装的插件，或者输入插件名
> - SideBarEnhancements: 扩展了侧边栏中菜单选项的数量，从而提升你的工作效率。
> - Anaconda：自动匹配关键字等实用功能，有效提高开发效率

