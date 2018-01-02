<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<?php 
	$title = 'Статистика игрока '.$_GET['name'];
	$main = '';
	$rules = '';
	$about = '';
	$faq = '';
	$member = '';
	include ("blocks/header.php");
?>
<div class="mainbody">


<?php 
if(isset($_GET['name']))
{
	echo('<center><img width="40" src=https://crafatar.com/renders/head/'.$_GET['name'].'?helm&scale=10 width=\'30\'>');
	$mojangJson = 'https://api.mojang.com/users/profiles/minecraft/'.$_GET['name'];

	$Mojangfile = file_get_contents($mojangJson);
	$MojangArray = json_decode($Mojangfile,true);
	$id = $MojangArray['id'];
	$hypixelJson = 'https://api.hypixel.net/player?key=83c62ae1-e1bd-4c55-b99b-8d7c0b6451fe&uuid='.$id;
	$file = file_get_contents($hypixelJson);
	$hypixelArray = json_decode($file,true);
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
	
	echo('<font size="7">'.$playerName.'</font></center>');
	echo('<img src="https://gen.plancke.io/exp/'.$_GET['name'].'.png">');
}
else { 
   echo('В адресной строке нет имени игрока!');
  }

?>
</div>


<?php
	include("blocks/footer.php");
?>
