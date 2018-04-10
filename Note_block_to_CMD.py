# Spectial for Azerus Team
# Created by Sirboys




from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_String
from pymclevel import TileEntity
from pymclevel.materials import alphaMaterials
import numpy


displayName = "Note Block to CMD"
Pitches = [0.5, 0.53, 0.56, 0.59, 0.62, 0.67, 0.7, 0.75, 0.8, 0.84, 0.9, 0.95, 1.0, 1.05, 1.12, 1.19, 1.26, 1.34, 1.42, 1.5, 1.6, 1.68, 1.78, 1.88, 2.0]



#def CreateChestItem(itemid, damage=0, count=1, slot=0):
 #   item = TAG_Compound()
   # item["id"] = TAG_Short(itemid)
  #  item["Damage"] = TAG_Short(damage)
 #   item["Count"] = TAG_Byte(count)
#    item["Slot"] = TAG_Byte(slot)
 #   return item

def perform(level,box,options):
	for x in xrange (box.minx,box.maxx):
		for y in xrange (box.miny,box.maxy):
			for z in xrange (box.minz,box.maxz):
				if level.blockAt(x,y,z) == 25 :
					if level.blockAt(x,y-1,z) == 3 or level.blockAt(x,y-1,z) == 0 or level.blockAt(x,y-1,z) == 22:
						mcnote = "minecraft:block.note.harp"
						noteBlock = level.tileEntityAt(x, y, z)
						if noteBlock["note"] == TAG_Byte(0):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[0]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(1):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[1]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(2):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[2]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(3):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[3]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(4):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[4]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(5):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[5]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(6):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[6]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(7):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[7]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(8):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[8]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(9):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[9]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(10):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[10]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(11):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[11]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(12):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[12]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(13):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[13]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(14):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[14]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(15):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[15]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(16):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[16]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(17):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[17]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(18):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[18]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(19):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[19]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(20):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[20]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(21):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[21]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(22):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[22]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(23):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[23]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(24):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[24]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
					if level.blockAt(x,y-1,z) == 5 or level.blockAt(x,y-1,z) == 86 or level.blockAt(x,y-1,z) == 54 or level.blockAt(x,y-1,z) == 58 :
						mcnote = "minecraft:block.note.bass"
						noteBlock = level.tileEntityAt(x, y, z)
						if noteBlock["note"] == TAG_Byte(0):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[0]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(1):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[1]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(2):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[2]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(3):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[3]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(4):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[4]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(5):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[5]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(6):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[6]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(7):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[7]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(8):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[8]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(9):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[9]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(10):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[10]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(11):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[11]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(12):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[12]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(13):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[13]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(14):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[14]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(15):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[15]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(16):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[16]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(17):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[17]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(18):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[18]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(19):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[19]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(20):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[20]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(21):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[21]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(22):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[22]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(23):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[23]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(24):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[24]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)	
					if level.blockAt(x,y-1,z) == 1 or level.blockAt(x,y-1,z) == 4 or level.blockAt(x,y-1,z) == 54 or level.blockAt(x,y-1,z) == 49 or  level.blockAt(x,y-1,z) == 7 or  level.blockAt(x,y-1,z) == 87 or  level.blockAt(x,y-1,z) == 45 :
						mcnote = "minecraft:block.note.basedrum"
						noteBlock = level.tileEntityAt(x, y, z)
						if noteBlock["note"] == TAG_Byte(0):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[0]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(1):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[1]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(2):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[2]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(3):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[3]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(4):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[4]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(5):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[5]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(6):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[6]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(7):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[7]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(8):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[8]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(9):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[9]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(10):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[10]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(11):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[11]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(12):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[12]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(13):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[13]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(14):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[14]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(15):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[15]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(16):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[16]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(17):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[17]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(18):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[18]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(19):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[19]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(20):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[20]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(21):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[21]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(22):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[22]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(23):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[23]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(24):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[24]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)		
					if level.blockAt(x,y-1,z) == 21 or level.blockAt(x,y-1,z) == 252 or level.blockAt(x,y-1,z) == 13 or level.blockAt(x,y-1,z) == 88 :
						mcnote = "minecraft:block.note.snare"
						noteBlock = level.tileEntityAt(x, y, z)
						if noteBlock["note"] == TAG_Byte(0):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[0]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(1):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[1]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(2):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[2]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(3):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[3]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(4):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[4]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(5):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[5]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(6):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[6]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(7):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[7]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(8):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[8]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(9):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[9]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(10):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[10]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(11):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[11]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(12):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[12]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(13):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[13]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(14):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[14]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(15):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[15]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(16):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[16]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(17):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[17]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(18):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[18]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(19):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[19]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(20):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[20]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(21):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[21]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(22):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[22]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(23):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[23]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(24):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[24]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)	
					if level.blockAt(x,y-1,z) == 89 or level.blockAt(x,y-1,z) == 20 or level.blockAt(x,y-1,z) == 95 :
						mcnote = "minecraft:block.note.hat"
						noteBlock = level.tileEntityAt(x, y, z)
						if noteBlock["note"] == TAG_Byte(0):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[0]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(1):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[1]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(2):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[2]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(3):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[3]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(4):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[4]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(5):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[5]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(6):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[6]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(7):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[7]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(8):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[8]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(9):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[9]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(10):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[10]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(11):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[11]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(12):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[12]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(13):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[13]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(14):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[14]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(15):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[15]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(16):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[16]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(17):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[17]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(18):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[18]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(19):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[19]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(20):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[20]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(21):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[21]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(22):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[22]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(23):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[23]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(24):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[24]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)		
					if level.blockAt(x,y-1,z) == 35 :
						mcnote = "minecraft:block.note.guitar"
						noteBlock = level.tileEntityAt(x, y, z)
						if noteBlock["note"] == TAG_Byte(0):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[0]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(1):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[1]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(2):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[2]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(3):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[3]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(4):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[4]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(5):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[5]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(6):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[6]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(7):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[7]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(8):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[8]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(9):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[9]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(10):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[10]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(11):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[11]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(12):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[12]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(13):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[13]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(14):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[14]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(15):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[15]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(16):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[16]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(17):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[17]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(18):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[18]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(19):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[19]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(20):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[20]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(21):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[21]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(22):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[22]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(23):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[23]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(24):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[24]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)			
					if level.blockAt(x,y-1,z) == 82 :
						mcnote = "minecraft:block.note.flute"
						noteBlock = level.tileEntityAt(x, y, z)
						if noteBlock["note"] == TAG_Byte(0):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[0]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(1):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[1]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(2):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[2]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(3):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[3]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(4):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[4]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(5):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[5]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(6):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[6]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(7):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[7]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(8):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[8]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(9):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[9]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(10):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[10]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(11):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[11]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(12):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[12]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(13):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[13]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(14):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[14]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(15):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[15]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(16):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[16]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(17):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[17]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(18):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[18]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(19):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[19]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(20):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[20]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(21):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[21]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(22):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[22]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(23):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[23]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(24):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[24]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)	
					if level.blockAt(x,y-1,z) == 41 :
						mcnote = "minecraft:block.note.bell"
						noteBlock = level.tileEntityAt(x, y, z)
						if noteBlock["note"] == TAG_Byte(0):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[0]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(1):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[1]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(2):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[2]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(3):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[3]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(4):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[4]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(5):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[5]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(6):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[6]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(7):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[7]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(8):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[8]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(9):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[9]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(10):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[10]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(11):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[11]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(12):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[12]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(13):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[13]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(14):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[14]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(15):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[15]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(16):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[16]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(17):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[17]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(18):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[18]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(19):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[19]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(20):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[20]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(21):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[21]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(22):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[22]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(23):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[23]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(24):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[24]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)	
					if level.blockAt(x,y-1,z) == 174 :
						mcnote = "minecraft:block.note.chime"
						noteBlock = level.tileEntityAt(x, y, z)
						if noteBlock["note"] == TAG_Byte(0):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[0]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(1):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[1]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(2):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[2]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(3):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[3]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(4):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[4]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(5):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[5]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(6):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[6]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(7):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[7]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(8):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[8]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(9):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[9]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(10):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[10]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(11):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[11]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(12):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[12]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(13):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[13]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(14):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[14]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(15):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[15]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(16):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[16]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(17):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[17]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(18):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[18]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(19):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[19]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(20):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[20]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(21):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[21]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(22):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[22]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(23):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[23]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(24):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[24]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)		
					if level.blockAt(x,y-1,z) == 216 :
						mcnote = "minecraft:block.note.xylophone"
						noteBlock = level.tileEntityAt(x, y, z)
						if noteBlock["note"] == TAG_Byte(0):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[0]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(1):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[1]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(2):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[2]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(3):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[3]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(4):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[4]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(5):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[5]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(6):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[6]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(7):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[7]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(8):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[8]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(9):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[9]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(10):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[10]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(11):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[11]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(12):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[12]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(13):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[13]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(14):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[14]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(15):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[15]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(16):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[16]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(17):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[17]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(18):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[18]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(19):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[19]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(20):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[20]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(21):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[21]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(22):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[22]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(23):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[23]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)
						if noteBlock["note"] == TAG_Byte(24):
							level.setBlockAt(x, y, z, 137)
							control = level.tileEntityAt(x, y, z)
							level.tileEntityAt(x, y, z)["Command"] = TAG_String(u'/execute @a[score_music=1,score_music_min=1] ~ ~ ~ /playsound {0} master @a[score_music=1,score_music_min=1] ~ ~ ~ 1 {1}'. format(mcnote, Pitches[24]))
						#	level.tileEntityAt(x, y, z)["note"].removeTileEntities
							level.tileEntityAt(x, y, z)["id"] = TAG_String(u'minecraft:command_block')
							level.tileEntityAt(x, y, z)["CustomName"] = TAG_String(u'@')
							level.tileEntityAt(x, y, z)["SuccessCount"] = TAG_Int(0)
							level.tileEntityAt(x, y, z)["x"] = TAG_Int(x)
							level.tileEntityAt(x, y, z)["y"] = TAG_Int(y)
							level.tileEntityAt(x, y, z)["z"] = TAG_Int(z)		
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
	

