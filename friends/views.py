from django.shortcuts import render
from django.http import JsonResponse
from .models import User, FriendRequest


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.create(username=username)
        return JsonResponse({'user_id': user.id})
    return render(request, 'registration.html')


def send_friend_request(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('friend_id')
        sender_id = request.POST.get('user_id')
        status = 'pending'
        friend_request = FriendRequest(status=status,
                                       sender_id=sender_id,
                                       receiver_id=receiver_id)
        friend_request.save()
        return JsonResponse({'success': True})
    return render(request, 'send_request.html')

