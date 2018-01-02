<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<?php 
	$title = "Участники";
	$main = '';
	$rules = '';
	$about = '';
	$faq = '';
	$member = 'class="item_active"';
	include ("blocks/header.php");
	
	
	
	
	
	?>
<div class="mainbody">

<div class='table_blur'>
<style>
table{
	width: 100%;
}
.table_blur {
  background: #f5ffff;
  border-collapse: collapse;
  text-align: left;
}
.table_blur th {
  border-top: 1px solid #777777;	
  border-bottom: 1px solid #777777; 
  box-shadow: inset 0 1px 0 #999999, inset 0 -1px 0 #999999;
  background: linear-gradient(#9595b6, #5a567f);
  color: white;
  padding: 10px 15px;
  position: relative;
}
.table_blur th:after {
  content: "";
  display: block;
  position: absolute;
  left: 0;
  top: 25%;
  height: 25%;
  width: 100%;
  background: linear-gradient(rgba(255, 255, 255, 0), rgba(255,255,255,.08));
}
.table_blur tr:nth-child(odd) {
  background: #ebf3f9;
}
.table_blur th:first-child {
  border-left: 1px solid #777777;	
  border-bottom:  1px solid #777777;
  box-shadow: inset 1px 1px 0 #999999, inset 0 -1px 0 #999999;
}
.table_blur th:last-child {
  border-right: 1px solid #777777;
  border-bottom:  1px solid #777777;
  box-shadow: inset -1px 1px 0 #999999, inset 0 -1px 0 #999999;
}
.table_blur td {
  position: relative;
  transition: all 0.5s ease;
}
.memberName{
    color: #AAAAAA;
	
}
</style>



<?php


	const EXP_FIELD = "networkExp";
    const LVL_FIELD = "networkLevel";
    const BASE = 10000;
    const GROWTH = 2500;
    /* Constants to generate the total amount of XP to complete a level */
    const HALF_GROWTH = 0.5 * GROWTH;
    /* Constants to look up the level from the total amount of XP */
    const REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH;
    const REVERSE_CONST = REVERSE_PQ_PREFIX * REVERSE_PQ_PREFIX;
    const GROWTH_DIVIDES_2 = 2 / GROWTH;
	


//if(isset($_POST['submit'])){
//	$ign = $_POST["ign"];
//	$file = 'http://api.mojang.com/users/profiles/minecraft/'.$ign;
//	$mojang = file_get_contents($file);
//	$mojangArray = json_decode($mojang, true);
//	if($mojang !=null){
//		$playerUuid = $mojangArray["id"];
//	$hypixelJson = 'https://api.hypixel.net/player?key=ee116a14-3a19-47bf-a4a3-6394928f564c&uuid=63a91ed9a480454696d8e000678f61e2';
  //  $file = file_get_contents($hypixelJson);
	//	$hypixelArray = json_decode($file,true);
	//	echo "Имя: ".$hypixelArray['player']['displayname'];
		
	//	echo "LVL: ".$hypixelArray['player']['networkLevel'];
		
	//	echo "Последний заход: ".$hypixelArray['player']['lastLogin'];
	//	print_r ($hypixelArray);
	//}
	$hypixelJsonGuild = 'https://api.hypixel.net/guild?key=83c62ae1-e1bd-4c55-b99b-8d7c0b6451fe&id=599b32290cf28c422200ead7';
	$fileGuild = file_get_contents($hypixelJsonGuild);
	$hypixelArrayGuild = json_decode($fileGuild,true);
	$sizeMembers = sizeof($hypixelArrayGuild['guild']['members']);
	//print_r ($hypixelArrayGuild);
	
	
//	print_r($hypixelArrayGuild);
	?>
<table cellpadding="5">
    <tr>
		<th>Скин</th>
        <th>Ник</th>
        <th>Звание</th>
		<th>Уровень</th>
        <th style="width:100px">Собранно Guild Coins вчера</th>
		<th style="width:100px">Собранно Guild Coins за сегодня</th>
        <th>Дата вступления</th>
		<th>Последний заход</th>
    </tr>
    
	<?php

    for($i = 0; $i < $sizeMembers; $i++){
	$hypixelJson = 'https://api.hypixel.net/player?key=83c62ae1-e1bd-4c55-b99b-8d7c0b6451fe&uuid='.$hypixelArrayGuild['guild']['members'][$i]['uuid'];
	$file = file_get_contents($hypixelJson);
	$hypixelArray = json_decode($file,true);	
	$exp = 	$hypixelArray['player']['networkExp'];
		

	//	print_r($mojangArray); https://crafatar.com/renders/head/Azeruss?helm&scale=10
	$dateVchera = date("d")-1;
	$dateSegodnya = date("d");
	$trueMonth = date("m")-1;
	
	
	//$exp = 79342431;

     $level = $exp < 0 ? 1 : floor(1 + REVERSE_PQ_PREFIX + sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * $exp)); 
	// echo $level;
	
	$coinsVchera = 0;
	$coinsSegodnia = 0;
	
	if($hypixelArrayGuild['guild']['members'][$i]['dailyCoins-'.$dateVchera.'-'.$trueMonth.date("-Y")] != null){
		$coinsVchera = $hypixelArrayGuild['guild']['members'][$i]['dailyCoins-'.$dateVchera.'-'.$trueMonth.date("-Y")];
		
	}
	if($hypixelArrayGuild['guild']['members'][$i]['dailyCoins-'.$dateSegodnya.'-'.$trueMonth.date("-Y")] != null){
		$coinsSegodnia = $hypixelArrayGuild['guild']['members'][$i]['dailyCoins-'.$dateSegodnya.'-'.$trueMonth.date("-Y")];
		
	}
	
	$playerName = $hypixelArray['player']['displayname'];
	$rankColor = $hypixelArray['player']['rankPlusColor'];
	if($hypixelArray['player']['newPackageRank'] == VIP){
		$playerName = '<span style=\'color:#3CE63C\'>[VIP] '.$playerName;
	}
	
	if($hypixelArray['player']['newPackageRank'] == VIP_PLUS){
		$playerName = '<span style=\'color:#3CE63C\'>[VIP</span><span style=\'color:#FFAA00\'>+</span><span style=\'color:#3CE63C\'></span><span style=\'color:#3CE63C\'>] '.$playerName;
	}
	if($hypixelArray['player']['newPackageRank'] == MVP){
		$playerName = '<span style=\'color:#3CE6E6\'>[MVP] '.$playerName;
	}
	if($hypixelArray['player']['newPackageRank'] == MVP_PLUS){
		if($rankColor == null){
			$rankColor = 'red';
		}
		if($rankColor == 'LIGHT_PURPLE'){
			$rankColor = '#FF55FF';
		}
		if($rankColor == 'DARK_GRAY'){
			$rankColor = '#555555';
		}
		if($rankColor == 'DARK_AQUA'){
			$rankColor = '#00AAAA';
		}
		if($rankColor == 'DARK_GREEN'){
			$rankColor = '#008000';
		}
		if($rankColor == 'DARK_PURPLE'){
			$rankColor = '#AA00AA';
		}
		
		
		$playerName = '<span style=\'color:#3CE6E6\'>[MVP</span><span style=\'color:'.$rankColor.'\'>+</span><span style=\'color:#3CE6E6\'>] '.$playerName;
	}
	if($hypixelArray['player']['newPackageRank'] == null){
		$playerName = '<span style=\'color:#AAAAAA\'>'.$playerName;
		
	}
	if($hypixelArray['player']['displayname'] == 'Sirboys'){
		$playerName = '<span style=\'color:#ff0000\'> [CODER] '.$hypixelArray['player']['displayname'];
	}
	// <a href="http://nuestraarmy.top/players.php?name="></a>
		echo '<tr>
		        <td width="30"><img src=https://crafatar.com/renders/head/'.$hypixelArray['player']['displayname'].'?helm&scale=10 width=\'30\'></td> 
				<td><p class="minecraftname"><a href="http://nuestraarmy.top/players.php?name='.$hypixelArray['player']['displayname'].'">'.$playerName.'</a></span></p></td>
				<td>'.$hypixelArrayGuild['guild']['members'][$i]['rank'].'</td>
				<td>'.$level.'</td>
				<td>'.$coinsVchera.'</td>
				<td>'.$coinsSegodnia.'</td>     
				<td>'.date("Y-m-d H:i",$hypixelArrayGuild['guild']['members'][$i]['joined']/1000).'</td>
				<td>'.date("Y-m-d H:i",$hypixelArray['player']['lastLogin']/1000).'</td>
				</tr>';
	}


?>
    </tbody>
</table>
	</div>
	
 
</div>
<?php 
	include ("blocks/footer.php")
?>
</div>

</body>
</html>