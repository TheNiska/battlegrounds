from models.pygame_game import PyGame
import custom_cards as cc


game = PyGame()

game.top_board = [cc.Annoy_o_Tron(), cc.Annoy_o_Tron(), cc.Dozy_Whelp()]
game.bottom_board = [cc.Dozy_Whelp(), cc.Annoy_o_Tron(), cc.Annoy_o_Tron()]

for crd in game.top_board:
    crd.stats_font = game.stats_font
    crd.text_font = game.text_font
for crd in game.bottom_board:
    crd.stats_font = game.stats_font
    crd.text_font = game.text_font

game.run()
