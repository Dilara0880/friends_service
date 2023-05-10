from django.shortcuts import render, redirect
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
    return render(request, 'sent_request.html')


def handle_request(request, friend_request_id, action):
    friend_request = FriendRequest.objects.get(id=friend_request_id)

    if friend_request.receiver == request.user:
        if action == 'accept':
            friend_request.status = 'accepted'
            friend_request.save()
        elif action == 'reject':
            friend_request.status = 'rejected'
            friend_request.save()

    return redirect(friend_request_list)


def friend_request_list(request):
    friend_requests = FriendRequest.objects.filter(receiver=request.user)

    context = {
        'friend_requests': friend_requests
    }

    return render(request, 'sent_request.html', context)





