import import_data as i
import export_data as ed
import UI

def choice_import_or_export():
	info = UI.get_info()
	if info == 'import':
		i.import_file()
	elif info == 'export':
		ed.export_file(UI.chose_format())