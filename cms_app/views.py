from django.http import HttpResponse
from django import template
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import ChurchMember
from .models import Payment
from .models import Document
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django import template
from django.contrib import messages

@csrf_exempt
def add_member(request):
    if request.method == 'POST':

        profile_image = request.FILES.get('profile_image')
        surname = request.POST['surname'].lower()
        other_name = request.POST['other_name'].lower()
        first_name = request.POST['first_name'].lower()
        house_address = request.POST['house_address']
        digital_address = request.POST['digital_address']
        phone_number = request.POST['phone_number']
        emergency_contact_number = request.POST['emergency_contact_number']
        hometown = request.POST['hometown']
        date_of_birth = request.POST['date_of_birth'].lower()
        gender = request.POST['gender']
        nationality = request.POST['nationality']
        martial_status = request.POST['martial_status']
        if_married = request.POST['if_married']
        spouse_name = request.POST['spouse_name']
        number_of_children = request.POST['number_of_children']
        children_names = request.POST['children_names']
        mother_name = request.POST['mother_name']
        is_mother_alive = request.POST['is_mother_alive']
        mother_religious_denomination = request.POST[
            'mother_religious_denomination']
        father_name = request.POST['father_name']
        is_father_alive = request.POST['is_father_alive']
        father_religious_denomination = request.POST[
            'father_religious_denomination']
        place_of_employment = request.POST['place_of_employment']
        position = request.POST['position']
        baptized = request.POST['baptized']
        baptized_place = request.POST['baptized_place']
        confirmed = request.POST['confirmed']
        confirmation_place = request.POST['confirmation_place']
        number_of_society = request.POST['number_of_society']
        society = request.POST['society']

        # Check if member already exists based on the specified fields
        # Check if member already exists based on the specified fields
        if ChurchMember.objects.filter(surname__iexact=surname, other_name__iexact=other_name, first_name__iexact=first_name, date_of_birth__iexact=date_of_birth).exists():
            messages.error(request, 'The data is already in the system.' )
            return redirect('add_member')

        churchmember = ChurchMember(
            profile_image=profile_image,
            surname=surname,
            other_name=other_name,
            first_name=first_name,
            house_address=house_address,
            digital_address=digital_address,
            phone_number=phone_number,
            emergency_contact_number=emergency_contact_number,
            hometown=hometown,
            date_of_birth=date_of_birth,
            gender=gender,
            nationality=nationality,
            martial_status=martial_status,
            if_married=if_married,
            spouse_name=spouse_name,
            number_of_children=number_of_children,
            children_names=children_names,
            mother_name=mother_name,
            is_mother_alive=is_mother_alive,
            mother_religious_denomination=mother_religious_denomination,
            father_name=father_name,
            is_father_alive=is_father_alive,
            father_religious_denomination=father_religious_denomination,
            place_of_employment=place_of_employment,
            position=position,
            baptized=baptized,
            baptized_place=baptized_place,
            confirmed=confirmed,
            confirmation_place=confirmation_place,
            number_of_society=number_of_society,
            society=society
        )
        churchmember.save()
        # return redirect('stats')  # Redirect to the 'stats' view
        messages.success(request, 'Member added successfully.')

    return render(request, 'add_member.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('stats')
        else:
            error = 'Invalid username or password'
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')


def stats(request):
    total_members = ChurchMember.objects.count()

    male_count = ChurchMember.objects.filter(gender='Male').count()

    female_count = ChurchMember.objects.filter(gender='Female').count()

    mother_catholic = ChurchMember.objects.filter(
        mother_religious_denomination='Catholics').count()

    mother_other = ChurchMember.objects.filter(
        mother_religious_denomination='Other').count()

    father_catholic = ChurchMember.objects.filter(
        father_religious_denomination='Catholics').count()

    father_other = ChurchMember.objects.filter(
        father_religious_denomination='Other').count()

    single = ChurchMember.objects.filter(
        martial_status='Single').count()

    married = ChurchMember.objects.filter(
        martial_status='Married').count()

    widowed = ChurchMember.objects.filter(
        martial_status='Widowed').count()
    
    nothing = ChurchMember.objects.filter(
        if_married ='Nothing').count()

    holy = ChurchMember.objects.filter(
        if_married='Holy Matrimony').count()

    traditional = ChurchMember.objects.filter(
        if_married='Traditional Marriage').count()

    context = {
        'total_members': total_members,
        'male_count': male_count,
        'female_count': female_count,
        'mother_catholic': mother_catholic,
        'mother_other': mother_other,
        'father_catholic': father_catholic,
        'father_other': father_other,
        'single': single,
        'married': married,
        'widowed': widowed,
        'nothing': nothing,
        'holy': holy,
        'traditional': traditional,
    }

    return render(request, 'stats.html', context)


def view_member(request):
    members = ChurchMember.objects.all()
    return render(request, 'view_member.html', {'members': members})


def add_payment(request):
    if request.method == 'POST':
        # Retrieve the form data
        name = request.POST['name']
        # date = request.POST.get('date')
        amount = request.POST.get('amount')
        payment_type = request.POST.get('payment_type')

        # Save the data to the database or perform any necessary actions
        payment = Payment(name=name,
                        #   date=date,
                          amount=amount,
                          payment_type=payment_type)
        payment.save()
        print(payment)
        messages.success(request, 'Payment added successfully.')

    return render(request, 'add_payment.html', )



def view_payment(request):
    payments = Payment.objects.all()  # Fetch all payment objects from the database
    return render(request, 'view_payment.html', {'payments': payments})


def edit_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)

    if request.method == 'POST':
        # Retrieve the form data
        # payment.id_number = request.POST['id_number']
        payment.name = request.POST['name']
        # payment.date = request.POST['date']
        payment.amount = request.POST['amount']
        payment.payment_type = request.POST['payment_type']
        payment.save()
        # Replace 'payment_list' with the appropriate URL name for the payment list view
        return redirect('view_payment')

    return render(request, 'edit_payment.html', {'payment': payment})

def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)

    if request.method == 'POST':
        payment.delete()
        return redirect('payment_list')

    return render(request, 'delete_payment.html', {'payment': payment})


def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})


def document(request):
    if request.method == 'POST':
        document_name = request.POST['document_name'].lower()
        document_image = request.FILES['document_image']

        # Check if document already exists based on the specified fields
        if Document.objects.filter(document_name__iexact=document_name,).exists():
            messages.error(
                request, 'The document/file is already in the system. Please choose a different name for the file.')
            return redirect('document')

        document = Document(document_name=document_name,
                            document_image=document_image)
        document.save()

        return redirect('view_document')

    return render(request, 'document.html')


def view_document(request):
    documents = Document.objects.all()

    # document = Document.objects.get(id=document_id)
    return render(request, 'view_document.html', {'documents': documents})





# def view_document(request, document_id):
#     document = get_object_or_404(Document, pk=document_id)

#     return render(request, 'view_document.html', {'document': document})
