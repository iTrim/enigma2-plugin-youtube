from Plugins.Plugin import PluginDescriptor

from . import _, screenwidth


def main(session, **kwargs):
	from .YouTubeUi import YouTubeMain
	session.open(YouTubeMain)

#add Youtube to Main Menu
def menu(menuid, **kwargs):
    if menuid == 'mainmenu':
        return [(_('YouTube'), main, 'YouTube', 44)]
    return []


def Plugins(**kwargs):
	if screenwidth == 'svg':
		icon = 'YouTube.svg'
	elif screenwidth == 1920:
		icon = 'YouTube_FHD.png'
	else:
		icon = 'YouTube_HD.png'
	#Adjusted for Main Menu	
	return [PluginDescriptor(name=_('YouTube'), description=_('Watch YouTube videos'), where = [PluginDescriptor.WHERE_PLUGINMENU],icon=icon,fnc=main),
			PluginDescriptor(name=_('YouTube'), description=_('Watch YouTube videos'), where = [PluginDescriptor.WHERE_EXTENSIONSMENU],icon=icon,fnc=main),
			PluginDescriptor(name=_('YouTube'), description=_('Watch YouTube videos'), where = [PluginDescriptor.WHERE_MENU],fnc=menu)]
