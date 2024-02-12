from django.shortcuts import get_object_or_404, render, redirect
from .models import Game
from users.models import User
from courts.models import Court


def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})


def game_detail(request, gameID):
    game = get_object_or_404(Game, gameID=gameID)
    return render(request, 'games/game_detail.html', {'game': game})


def game_create(request):
    if request.method == "POST":
        court_id = request.POST.get('court')
        court = Court.objects.get(id=court_id)
        game = Game.objects.create(court=court)
        # Assuming 'players' is a list of user IDs from the form
        players_ids = request.POST.getlist('players')
        for player_id in players_ids:
            user = User.objects.get(playerID=player_id)
            game.players_associated.add(user)
        return redirect('game_detail', gameID=game.gameID)
    return render(request, 'games/game_edit.html', {})


def game_edit(request, gameID):
    game = get_object_or_404(Game, gameID=gameID)
    if request.method == "POST":
        # Similar process as game_create for updating fields
        # Remember to handle changes to many-to-many fields properly
        return redirect('game_detail', gameID=game.gameID)
    return render(request, 'games/game_edit.html', {'game': game})


def game_delete(request, gameID):
    game = get_object_or_404(Game, gameID=gameID)
    if request.method == "POST":
        game.delete()
        return redirect('game_list')
    return render(request, 'games/game_confirm_delete.html', {'game': game})


def user_games(request, user_id):
    games = Game.objects.get_games_for_user(user_id)
    return render(request, 'games/user_games_list.html', {'games': games, 'user_id': user_id})
