#include "BIS_AddonInfo.hpp"
class CfgPatches
{
class FDF_VOICES_A3
	{
	units[] = {};
	weapons[] = {};
	requiredVersion = 0.1;
	requiredAddons[] = {};
	};
};
class CfgIdentities
{
	class Male01
	{
	name = "Male01";
	glasses = "None";
	speaker = "Male01FIN_FDF"; // your voice class defined below
	pitch = 1;
	nameSound = "Kelly"; // I believe this ties to the sound file for Kerry, I'm guessing you can change this but I havent bothered
	};
};

class CfgVoice
{
	voices[] + = {"Male01FIN","Male02FIN","Male03FIN","Male04FIN","Male05FIN","Male06FIN","Male07FIN","Male08FIN","Male09FIN","Female01FIN"};
	micOuts[] = {off1.ogg};
	preview = "preview.ogg"; // I think this doesn't work in actual arma 3
	default = "Male01FIN_FDF";
	class FIN;
	class Male01FIN_FDF: FIN
	{
		protocol = "RadioProtocolENG";
		directories[] = {"\FDFVOICES\Male01FIN\","\FDFVOICES\Male01FIN\"};
		identityTypes[] = {"Clone"};
		scope = 2;
		icon = "\FDFVOICES\flag.paa";
		displayName = "Finnish 01";
		author = "FDF Team (converted to Arma3 by phewi)";
	};
	class Male02FIN_FDF: FIN
	{
		protocol = "RadioProtocolENG";
		directories[] = {"\FDFVOICES\Male02FIN\","\FDFVOICES\Male02FIN\"};
		identityTypes[] = {"Clone"};
		scope = 2;
		icon = "\FDFVOICES\flag.paa";
		displayName = "Finnish 02";
		author = "FDF Team (converted to Arma3 by phewi)";
	};
		class Male03FIN_FDF: FIN
	{
		protocol = "RadioProtocolENG";
		directories[] = {"\FDFVOICES\Male03FIN\","\FDFVOICES\Male03FIN\"};
		identityTypes[] = {"Clone"};
		scope = 2;
		icon = "\FDFVOICES\flag.paa";
		displayName = "Finnish 03";
		author = "FDF Team (converted to Arma3 by phewi)";
	};
	class Male04FIN_FDF: FIN
	{
		protocol = "RadioProtocolENG";
		directories[] = {"\FDFVOICES\Male04FIN\","\FDFVOICES\Male04FIN\"};
		identityTypes[] = {"Clone"};
		scope = 2;
		icon = "\FDFVOICES\flag.paa";
		displayName = "Finnish 04";
		author = "FDF Team (converted to Arma3 by phewi)";
	};
	class Male05FIN_FDF: FIN
	{
		protocol = "RadioProtocolENG";
		directories[] = {"\FDFVOICES\Male05FIN\","\FDFVOICES\Male05FIN\"};
		identityTypes[] = {"Clone"};
		scope = 2;
		icon = "\FDFVOICES\flag.paa";
		displayName = "Finnish 05";
		author = "FDF Team (converted to Arma3 by phewi)";
	};
	class Male06FIN_FDF: FIN
	{
		protocol = "RadioProtocolENG";
		directories[] = {"\FDFVOICES\Male06FIN\","\FDFVOICES\Male06FIN\"};
		identityTypes[] = {"Clone"};
		scope = 2;
		icon = "\FDFVOICES\flag.paa";
		displayName = "Finnish 06";
		author = "FDF Team (converted to Arma3 by phewi)";
	};
	class Male07FIN_FDF: FIN
	{
		protocol = "RadioProtocolENG";
		directories[] = {"\FDFVOICES\Male07FIN\","\FDFVOICES\Male07FIN\"};
		identityTypes[] = {"Clone"};
		scope = 2;
		icon = "\FDFVOICES\flag.paa";
		displayName = "Finnish 07";
		author = "FDF Team (converted to Arma3 by phewi)";
	};
	class Male08FIN_FDF: FIN
	{
		protocol = "RadioProtocolENG";
		directories[] = {"\FDFVOICES\Male08FIN\","\FDFVOICES\Male08FIN\"};
		identityTypes[] = {"Clone"};
		scope = 2;
		icon = "\FDFVOICES\flag.paa";
		displayName = "Finnish 08";
		author = "FDF Team (converted to Arma3 by phewi)";
	};
	class Male09FIN_FDF: FIN
	{
		protocol = "RadioProtocolENG";
		directories[] = {"\FDFVOICES\Male09FIN\","\FDFVOICES\Male09FIN\"};
		identityTypes[] = {"Clone"};
		scope = 2;
		icon = "\FDFVOICES\flag.paa";
		displayName = "Finnish 09";
		author = "FDF Team (converted to Arma3 by phewi)";
	};
	class Female01FIN_FDF: FIN
	{
		protocol = "RadioProtocolENG";
		directories[] = {"\FDFVOICES\Female01FIN\","\FDFVOICES\Female01FIN\"};
		identityTypes[] = {"Clone"};
		scope = 2;
		icon = "\FDFVOICES\flag.paa";
		displayName = "Finnish 10 (Female)";
		author = "FDF Team (converted to Arma3 by phewi)";
	};
	
};
};