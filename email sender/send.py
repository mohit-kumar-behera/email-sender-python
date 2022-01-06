import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
MAIL_CONTENT_DIR_PATH = os.path.join(BASE_DIR, 'Mail_content')


class Template:
	template_content_name =  ""
	context_name = ""
	user_name = ""

	def __init__(self, template_content_name = "", context_name = "", user_name="",  *args, **kwargs):
		self.template_content_name = template_content_name
		self.context_name = context_name
		self.user_name = user_name


	def get_template(self):
		TEMPLATE_CONTENT_PATH = os.path.join(MAIL_CONTENT_DIR_PATH, self.template_content_name)
		if not os.path.exists(TEMPLATE_CONTENT_PATH):
			raise Exception("This path does Not Exist")

		# opening the file
		with open(TEMPLATE_CONTENT_PATH,'r') as f:
			template_content_data = f.read()

		return template_content_data


	def render_name_in_template(self, context_name = ''):
		put_content_name = self.context_name
		template_content_data = self.get_template()
		return template_content_data.format(receiver_name=put_content_name, user_name=self.user_name)
