import braintree
from decimal import Decimal
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .forms import DonateForm

if settings.DEBUG:
	braintree.Configuration.configure(braintree.Environment.Sandbox,
	  merchant_id=settings.BRAINTREE_MERCHANT_ID,
	  public_key=settings.BRAINTREE_PUBLIC,
	  private_key=settings.BRAINTREE_PRIVATE)
else:
	braintree.Configuration.configure(braintree.Environment.Production,
	  merchant_id=settings.BRAINTREE_MERCHANT_ID,
	  public_key=settings.BRAINTREE_PUBLIC,
	  private_key=settings.BRAINTREE_PRIVATE)



# Create your views here.
class DonationView(View):
	template = "donate/donate.html"
	form = DonateForm

	def get(self, request):
		if 'client_token' not in self.request.session:
			self.request.session['client_token']= braintree.ClientToken.generate()
		client_token = self.request.session.get('client_token')
		context ={
			"form": self.form(),
			"client_token": client_token
		}
		return render(request, self.template, context)


	def post(self, request):
		form = self.form(request.POST or None)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['donate_email']
			donation_amount = form.cleaned_data['donation_amount']
			donation_comment = form.cleaned_data['donation_comment']
			nonce = request.POST.get("payment_method_nonce")
			if nonce:
				result = braintree.Transaction.sale({
					"amount": Decimal(donation_amount),
					"payment_method_nonce": nonce,
					"options": {
						"submit_for_settlement": True
					}
				})
				if result.is_success:
					form.save()
					return redirect("share")
		data = {
			"form_errors": form.errors.as_json()
		}
		return JsonResponse(data, status=400)




