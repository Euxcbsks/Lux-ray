from core.extension.server import ExtensionServer

class ExclCatServer(ExtensionServer):
	def register_category(self, category_id, member_id):
		self._update({f"categories.{category_id}.owner_id": member_id})
