# -*- coding: utf-8 -*-
#物联1602 zjx
###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## 登陆界面
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"脑筋急转弯试玩版",
                          pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer = wx.BoxSizer(wx.VERTICAL)
# 第一行
        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"现在位于登陆界面！“这是个demo，1+2=3”分别暗示了用户名和密码",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)
# 第二行
        self.staticText1 = wx.StaticText(self, wx.ID_ANY, u"用户名：",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText1.Wrap(-1)

        bSizer11.Add(self.staticText1, 0, wx.ALL, 5)
        # 用户名
        self.textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, u"请输入用户名",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.textCtrl1, 0, wx.ALL, 5)

        bSizer.Add(bSizer11, 0, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)
# 第三行
        self.staticText2 = wx.StaticText(self, wx.ID_ANY, u"密码：    ",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText2.Wrap(-1)

        bSizer12.Add(self.staticText2, 0, wx.ALL, 5)
        # 密码
        self.textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, "...",
                                     wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_PASSWORD)
        bSizer12.Add(self.textCtrl2, 0, wx.ALL, 5)

        bSizer.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)
# 第四行
        self.button1 = wx.Button(self, wx.ID_ANY, u"登陆", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        bSizer13.Add(self.button1, 1, wx.ALL, 5)

        bSizer.Add(bSizer13, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button1.Bind(wx.EVT_BUTTON, self.loading1)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def loading1(self, event):
        # event.Skip()
        UserName = self.textCtrl1.GetValue()
        PassWord = self.textCtrl2.GetValue()
        if (UserName == 'demo') and (PassWord == '123'):
            self.Destroy()
            frame2 = MyFrame2()
            frame2.Show(True)


###########################################################################
## 第一关界面
###########################################################################

class MyFrame2(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"第一关",
                          pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"登陆界面居然别破解了！！！！",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText1 = wx.StaticText(self, wx.ID_ANY, u"问题：",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText1.Wrap(-1)

        bSizer11.Add(self.staticText1, 0, wx.ALL, 5)
        # 用户名
        self.staticText3 = wx.StaticText(self, wx.ID_ANY, u"日月潭的中间是什么？",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.staticText3, 0, wx.ALL, 5)

        bSizer.Add(bSizer11, 0, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText2 = wx.StaticText(self, wx.ID_ANY, u"答案：",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText2.Wrap(-1)

        bSizer12.Add(self.staticText2, 0, wx.ALL, 5)
        # 密码
        self.textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, "...",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.textCtrl2, 0, wx.ALL, 5)

        bSizer.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.button1 = wx.Button(self, wx.ID_ANY, u"提交", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        bSizer13.Add(self.button1, 1, wx.ALL, 5)

        bSizer.Add(bSizer13, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # 事件
        self.button1.Bind(wx.EVT_BUTTON, self.loading1)

    def __del__(self):
        pass

    # 事件函数自己处理
    def loading1(self, event):
        # event.Skip()
        # UserName = self.textCtrl1.GetValue()
        PassWord = self.textCtrl2.GetValue()
        if PassWord == '月':
            self.Destroy()
            frame2 = MyFrame3()
            frame2.Show(True)


###########################################################################
## 第二关
###########################################################################

class MyFrame3(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"第二关",
                          pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"第一关也被破解了！oh my God!",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText1 = wx.StaticText(self, wx.ID_ANY, u"问题：",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText1.Wrap(-1)

        bSizer11.Add(self.staticText1, 0, wx.ALL, 5)
        # 用户名
        self.staticText3 = wx.StaticText(self, wx.ID_ANY, u"话梅、杨梅、草莓谁的打扮最不好看？",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.staticText3, 0, wx.ALL, 5)

        bSizer.Add(bSizer11, 0, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText2 = wx.StaticText(self, wx.ID_ANY, u"你的答案：    ",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText2.Wrap(-1)

        bSizer12.Add(self.staticText2, 0, wx.ALL, 5)
        # 密码
        self.textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, "...",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.textCtrl2, 0, wx.ALL, 5)

        bSizer.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.button1 = wx.Button(self, wx.ID_ANY, u"提交", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        bSizer13.Add(self.button1, 1, wx.ALL, 5)

        bSizer.Add(bSizer13, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # 事件
        self.button1.Bind(wx.EVT_BUTTON, self.loading1)

    def __del__(self):
        pass

    # 事件函数自己处理
    def loading1(self, event):
        # event.Skip()
        # UserName = self.textCtrl1.GetValue()
        PassWord = self.textCtrl2.GetValue()
        if PassWord == '杨梅':
            self.Destroy()
            frame2 = MyFrame4()
            frame2.Show(True)


###########################################################################
## 第三关
###########################################################################

class MyFrame4(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"第三关",
                          pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"YOU真是VERY厉害啊!!!",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText1 = wx.StaticText(self, wx.ID_ANY, u"问题：",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText1.Wrap(-1)

        bSizer11.Add(self.staticText1, 0, wx.ALL, 5)
        # 用户名
        self.staticText3 = wx.StaticText(self, wx.ID_ANY, u"什么动物可以贴在墙上？",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.staticText3, 0, wx.ALL, 5)

        bSizer.Add(bSizer11, 0, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText2 = wx.StaticText(self, wx.ID_ANY, u"你的答案：    ",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText2.Wrap(-1)

        bSizer12.Add(self.staticText2, 0, wx.ALL, 5)
        # 密码
        self.textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, "...",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.textCtrl2, 0, wx.ALL, 5)

        bSizer.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.button1 = wx.Button(self, wx.ID_ANY, u"提交", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        bSizer13.Add(self.button1, 1, wx.ALL, 5)

        bSizer.Add(bSizer13, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # 事件
        self.button1.Bind(wx.EVT_BUTTON, self.loading1)

    def __del__(self):
        pass

    # 事件函数自己处理
    def loading1(self, event):
        # event.Skip()
        # UserName = self.textCtrl1.GetValue()
        PassWord = self.textCtrl2.GetValue()
        if PassWord == '海豹':
            self.Destroy()
            frame2 = MyFrame5()
            frame2.Show(True)

###########################################################################
## 第四关
###########################################################################


class MyFrame5(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"第四关",
                          pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"em.................",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText1 = wx.StaticText(self, wx.ID_ANY, u"问题：",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText1.Wrap(-1)

        bSizer11.Add(self.staticText1, 0, wx.ALL, 5)
        # 用户名
        self.staticText3 = wx.StaticText(self, wx.ID_ANY, u"“太阳”的“太”去掉一点是什么字？",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.staticText3, 0, wx.ALL, 5)

        bSizer.Add(bSizer11, 0, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText2 = wx.StaticText(self, wx.ID_ANY, u"你的答案：    ",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText2.Wrap(-1)

        bSizer12.Add(self.staticText2, 0, wx.ALL, 5)
        # 密码
        self.textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, "...",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.textCtrl2, 0, wx.ALL, 5)

        bSizer.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.button1 = wx.Button(self, wx.ID_ANY, u"提交", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        bSizer13.Add(self.button1, 1, wx.ALL, 5)

        bSizer.Add(bSizer13, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # 事件
        self.button1.Bind(wx.EVT_BUTTON, self.loading1)

    def __del__(self):
        pass

    # 事件函数自己处理
    def loading1(self, event):
        # event.Skip()
        # UserName = self.textCtrl1.GetValue()
        PassWord = self.textCtrl2.GetValue()
        if PassWord == '人':
            self.Destroy()
            frame2 = MyFrame6()
            frame2.Show(True)


###########################################################################
## 结束
###########################################################################


class MyFrame6(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"最后",
                          pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"你居然通关了！！！恭喜！！！",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText2 = wx.StaticText(self, wx.ID_ANY, u"Thanks for your play!!!",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText2.Wrap(-1)

        bSizer12.Add(self.staticText2, 0, wx.ALL, 5)
        # 密码

        bSizer.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.button1 = wx.Button(self, wx.ID_ANY, u"关闭", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        bSizer13.Add(self.button1, 1, wx.ALL, 5)

        bSizer.Add(bSizer13, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # 事件
        self.button1.Bind(wx.EVT_BUTTON, self.loading1)

    def __del__(self):
        pass

    # 事件函数自己处理
    def loading1(self, event):
        self.Destroy()

###########################################################################
## 主函数
###########################################################################

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame1(parent=None)
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
