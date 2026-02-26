local data_path = ""
local daily = "N/A"
local monthly = "N/A"
local go_home = "N/A"
local mode = "normal"
local target_hours = "8:30"
local timestamp = "No data"

local function get_value(content, key)
    local pattern = '"' .. key .. '"%s*:%s*"(.-)"'
    return content:match(pattern)
end

function Initialize()
    data_path = SKIN:GetVariable("DataPath")
end

function Update()
    local file = io.open(data_path, "r")
    if not file then
        daily = "N/A"
        monthly = "N/A"
        go_home = "N/A"
        mode = "normal"
        target_hours = "8:30"
        timestamp = "file not found"
        return 0
    end

    local content = file:read("*a")
    file:close()

    daily = get_value(content, "daily_solde") or "N/A"
    monthly = get_value(content, "monthly_solde") or "N/A"
    go_home = get_value(content, "go_home") or "N/A"
    mode = get_value(content, "mode") or "normal"
    target_hours = get_value(content, "target_hours") or "8:30"

    local raw_time = get_value(content, "timestamp")
    if raw_time then
        timestamp = raw_time:gsub("T", " ")
    else
        timestamp = "N/A"
    end

    return 0
end

function GetDaily()
    return daily
end

function GetMonthly()
    return monthly
end

function GetGoHome()
    return go_home
end

function GetMode()
    if mode == "ramadan" then
        return "Ramadan"
    end
    return "Normal"
end

function GetTargetHours()
    return target_hours
end

function GetTimestamp()
    return timestamp
end
