local UiMakeLib = loadstring(game:HttpGet("https://raw.githubusercontent.com/Msunehub/Uilm/refs/heads/main/UiMat1.lua"))()
local Notify = UiMakeLib:MakeNotify({
	["Title"] = "NgMinhTuan",
	["Description"] = "Notification",
	["Color"] = Color3.fromRGB(151, 207, 23),
	["Content"] = "Welcome to Fluriore UI",
	["Time"] = 1,
	["Delay"] = 10
})
local Window = UiMakeLib:MakeGui({
	["NameHub"] = "Mtuan Hub",
	["Description"] = "Ver 1",
	["Color"] = Color3.fromRGB(151, 207, 23),
	["Logo Player"] = "https://www.roblox.com/headshot-thumbnail/image?userId="..game:GetService("Players").LocalPlayer.UserId .."&width=420&height=420&format=png",
	["Name Player"] = tostring(game:GetService("Players").LocalPlayer.Name),
	["Tab Width"] = 140
})
local Tab1 = Window:CreateTab({
	["Name"] = "Hack Chính",
	["Icon"] = "rbxassetid://7733960981"
})
local Tab2 = Window:CreateTab({
	["Name"] = "Cài đặt",
	["Icon"] = "rbxassetid://7734053495"
})
local Section = Tab1:AddSection("Mở Các Loại Hack")
local Paragraph = Section:AddParagraph({
	["Title"] = "Paragraph",
	["Content"] = "This is a Paragraph"
})
Paragraph:Set({
	["Title"] = "Paragraph",
	["Content"] = "This is a Paragraph"
})
local Toggle = Section:AddToggle({
	["Title"]= "Toggle",
	["Content"] = "This is a Toggle",
	["Default"] = false,
	["Multi"] = true,
	["Options"] = {"Option 1", "Option 2"},
	["Selecting"] = {"Option 1"},
	["Callback"] = function(Value) 
		print(Value)
	end
})
Toggle:Set(false)
print(Toggle.Value)
local Button = Section:AddButton({
	["Title"] = "Menu Hub",
	["Content"] = "Hỗ trợ máy yếu",
	["Icon"] = "rbxassetid://16932740082",
	["Callback"] = function()
	 loadstring(game:HttpGet("https://api.luarmor.net/files/v3/loaders/a5c3af437cd698d64379cf75cacb9281.lua"))()
	end
})
local Button = Section:AddButton({
	["Title"] = "Fix lag",
	["Content"] = "Hỗ trợ máy yếu",
	["Icon"] = "rbxassetid://16932740082",
	["Callback"] = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/TurboLite/Script/main/FixLag.lua"))()
	end
})
local Slider = Section:AddSlider({
	["Title"] = "Slider",
	["Content"] = "This is a Slider",
	["Min"] = 0,
	["Max"] = 100,
	["Increment"] = 1,
	["Default"] = 30,
	["Callback"] = function(Value) 
		print(Value)
	end
})
Slider:Set(30)
print(Slider.Value)
local Input = Section:AddInput({
	["Title"] = "Input",
	["Content"] = "This is a Input",
	["Callback"] = function(Value) 
		print(Value)
	end
})
Input:Set("Input TextBox")
print(Input.Value)
local Dropdown = Section:AddDropdown({
	["Title"] = "Dropdown",
	["Content"] = "This is a Dropdown",
	["Multi"] = false,
	["Options"] = {"Option 1", "Option 2"},
	["Default"] = {"Option 1"},
	["Callback"] = function(Value)
		print(Value)
	end
})
Dropdown:Set({"Option 1"})
Dropdown:AddOption("Option 3")
Dropdown:Clear()
Dropdown:Refresh({"Option 1", "Option 2"}, {"Option 1"})
print(Dropdown.Value)
print(Dropdown.Options)
