from core.rh.models import Aluno

class UserTypeMiddleware(object):

	def process_request(self, request):
		request.user.is_aluno = False
		if request.user.id != None:
			if Aluno.objects.filter(email=request.user.email):
				request.user.is_aluno = True
		if "email" in request.session:
			if Aluno.objects.filter(email=request.session['email']):
				request.user.is_aluno = True