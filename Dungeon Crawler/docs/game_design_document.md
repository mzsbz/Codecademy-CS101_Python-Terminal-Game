**Title:**  
Dungeon Crawler 
  
**Description:**  
Progress through random rooms until you die!  
    
---    
    
**[Conditions] Starting:**  
Start with 100 Health, 5 lockpicks and 0 gold. 
  
**[Conditions] Room Entry:**  
Each room has a door which can either be bashed down or picked.  
* Failing to bash door will damage you.  
* Failing to pick the lock will destroy 1 lockpick.  
* If player have 0 lockpicks, player can only attempt to bash the door
  
**[Conditions] Room Complete:**  
Apart from continuing to the next door:  
* Each enemy defeated grants player 5 gold.  
* Each treasure chest found grants player 5-25 gold  
* Each health fountain found grants player 10HP
  
---
  
**[Type] Room:**  
Each door spawns one type of room:  
| Name | Spawn Chance <= 10 Rooms | Spawn Chance > 10 Rooms |
|---|---|---|
| Enemy Lair | High | High |
| Treasure Room | Low | Med |
| Health Fountain | Med | Low |

**[Type] Enemy:**  
Each enemy lair spawns one type of enemy:
| Name | Health | Damage | Steal | Hit Chance | Spawn Chance <= 10 Rooms|  Spawn Chance > 10 Rooms |
|---|---|---|---|---|---|---|
| Rat | 10 | 1 | 0 | High | High | Low |
| Thief | 25 | 5 | 5-10 | Med | Med | Med |
| Blind Ogre | 50 | 25-50 | 0 | Low | Low | High |
  
---
  
**[Outcome] Game Over:**  
Upon dying, total number of rooms completed and total gold accrued is displayed.
  
