from TeamFightTacticsBot.Utility.BotController import bot_initialize
import TeamFightTacticsBot.Utility.Constants as Constants
import TeamFightTacticsBot.Utility.Utils as Utils
import TeamFightTacticsBot.Utility.ConfigFileLoader as ConfigFileLoader
from TeamFightTacticsBot.Structures.PlayingBoard import PlayingBoard
from PIL import Image
from TeamFightTacticsBot.Structures.LearnedMetaData import LearnedMetaData
from TeamFightTacticsBot.Enumerators.Champions import Champions
from TeamFightTacticsBot.Enumerators.Synergies import Synergies
import os


def start():
    if __name__ is not '__main__':
        return

    debugging = True

    if not debugging:
        Constants.variables_initialize(os.path.dirname(__file__))
        bot_initialize()

    if debugging:
        Utils.initialize_resources(os.path.dirname(__file__))
        ConfigFileLoader.write_config_file()
        board = PlayingBoard("Connor")
        board.board_slots[1][1] = Champions.MORDEKAISER.value
        Utils.buy_champions(Image.open("TestDuplicates2.png"), board)

        # print(str(get_items_carasel(test)))


start()
