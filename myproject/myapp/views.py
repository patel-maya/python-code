from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App

SLACK_APP_TOKEN = "xoxe.xoxp-1-Mi0yLTQ1ODUxODgxMDcwNDYtNDYxNTQ4MjkzODQwMC01MTQ5MTM0MjQ4MDM4LTUxNjg0OTUxNDM4MjUtYmM2MjEyMjc1MzRkMDFiMDFhZTY2YWIzYWRmYWI5NjQzNmQ2M2Y4NmRjN2U0ZDU0MGRjYWQzM2JiY2UxZjc3Ng"
SLACK_BOT_TOKEN = ""
SLACK_CHANNEL = "#general"

slack_client = WebClient(token=SLACK_BOT_TOKEN)
slack_app = App(token=SLACK_APP_TOKEN)

def send_slack_notification(message):
        response = slack_client.chat_postMessage(channel=SLACK_CHANNEL, text='some message')
        return HttpResponse(response)
    # except SlackApiError as e:
    #     print("Error sending message: {}".format(e))
class Send_Mail(APIView):
    def get(self, request):
        # data = self.request.POST.get()
        case = Case.objects.get(previous_organization=2)
        previous_org = case.previous_organization
        get_case = Case.objects.filter(referral_option=1).latest('created')
        # kpis = referral_action.kpis.all()
        organization = get_case.referral_option
        user_email = organization.org.all()
        kpi_list = []
        for users in user_email:
            get_case = Case.objects.filter(referral_option=1).latest('created')
            kpis = get_case.kpis.all()
        for kpi in kpis:
            kpi_id=kpi.id
            kpi_description=kpi.description
            kpi_level = kpi.level
            kpi_list.append({'id': kpi_id, 'description': kpi_description, 'level': kpi_level})
        message = ''
        message += f" Dear {organization.name}, Please be advised of the following cases being referred to you by {previous_org.name}\n"
        for kpi in kpi_list:
            # if previous_org:
            #     message += f" Dear {organization.name} Please be advised of the following cases being referred to you by {previous_org.name}\n"
            message += f"ID {kpi['id']}: Description {kpi['description']}: ({kpi['level']})\n"
        message += f"Please go to ILM system to find the information about this case for your action.\n Have a great day!"
        # message=kpi_data
        
        subject = 'New Message Referred to your organization'
        from_email = 'ilm@issarainstitute.org'
        list = [user.user.email for user in user_email]
        for mail in list:
            recipient_list = [mail]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return HttpResponse('Email sent successfully')

# def send_mail_function(request):
#     case = get_object_or_404(Case, previous_organization=2)
#     previous_org = case.previous_organization
#     print(previous_org)
#     get_case = Case.objects.filter(referral_option=1).latest('created')
#     organization = get_case.referral_option
#     print(organization)
#     user_email = organization.org.all()
#     kpi_list = []
#     for users in user_email:
#         get_case = Case.objects.filter(referral_option=1).latest('created')
#         kpis = get_case.kpis.all()
#     for kpi in kpis:
#         kpi_id=kpi.id
#         kpi_description=kpi.description
#         kpi_level = kpi.level
#         kpi_list.append({'id': kpi_id, 'description': kpi_description, 'level': kpi_level})
#     message = ''
#     for kpi in kpi_list:
#         if previous_org:
#             message += f" Dear {organization.name} Please be advised of the following cases being referred to you by {previous_org.name}\n"
#         message += f"ID {kpi['id']}: Description {kpi['description']}: ({kpi['level']})\n"
        
#     subject = 'New message from'
#     from_email = 'ilm@issarainstitute.org'
#     recipient_list = [user.user.email for user in user_email]
#     send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#     return HttpResponse('Email sent successfully')

class GetMessageApi(APIView):
    def post(self, request):
        org = request.data.get('org')
        case = request.data.get('case')
        case = Case.objects.get(id=case)
        new_organization = Organization.objects.get(id=org)
        case.referral_option = new_organization
        case.save()
        return HttpResponse({'case referred'})

    def get(self, request):
        # import pdb;pdb.set_trace()
        
        get_id = self.request.query_params.get('id')
        my_organization = Organization.objects.get(id=get_id)
        referred_cases = Case.objects.filter(referral_option=my_organization)
        previouse_organization = Case.objects.filter(case_created_by=request.user.id, previous_organization = self.request.query_params.get('id')) 
        serializer = CaseSerializer(referred_cases,many=True)
        # case=Case.objects.filter(referral_option=(Organization.objects.filter))
        # (created_at__in=(UserOrganization.objects.filter(user_id=request.user.id).values_list('organization_id',flat=True)).values_list('organization_id', flat=True))))
        return Response(serializer.data)

class CreateGrievanceView(APIView):
    def get(self, request):
        if request.user.type=='JS':
            grievance = Grievance.objects.filter(created_by=request.user.id)
            serializer = GrievanceSerializer(grievance, many=True)
            return Response({"grievance":serializer.data})
        if request.user.type=='EM':
            org =EmployerOrganizations.objects.get(employers=request.user.id)
            grievance = Grievance.objects.filter(employerorganization=org)
            serializer = GrievanceSerializer(grievance, many=True)
            return Response({"grievance":serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

    def post(self, request):
        org=EmployerOrganizations.objects.get(jobseeker=request.user.id)
        get_employer = org.employers.email
        serializer = GrievanceSerializer(data=request.data)
        if serializer.is_valid():
            grievance = serializer.save()
        subject = 'New grievance created'
        message =  request.data['message']
        # from_email = request.user.email
        from_email = 'testmailinator0105@gmail.com'
        # recipient_list = ['victa.app@gmail.com']
        recipient_list = [get_employer]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
        


        
        
