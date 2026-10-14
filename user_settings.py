#To enable these settings, name this file "user_settings.py".

#Settings here will take effect for all games run in this Proton version.

user_settings = {
    "__GL_MaxFramesAllowed": "1",

    "__GL_SYNC_TO_VBLANK": "1",

    "__GL_GSYNC_ALLOWED": "1",

    "PROTON_ENABLE_WAYLAND": "1",

    "PROTON_ENABLE_NGX_UPDATER": "1",

    "VKD3D_CONFIG": "dxr12,descriptor_heap",

    "DXVK_HDR" : "1",

    "DXVK_NVAPI_VKREFLEX": "1",

    "DXVK_NVAPI_DRS_NGX_DLSS_RR_OVERRIDE": "on",

    "DXVK_NVAPI_DRS_NGX_DLSS_SR_OVERRIDE": "on",

    "DXVK_NVAPI_DRS_NGX_DLSS_FG_OVERRIDE": "on",

    "DXVK_NVAPI_DRS_NGX_DLSS_RR_OVERRIDE_RENDER_PRESET_SELECTION": "RENDER_PRESET_F",

    "DXVK_NVAPI_DRS_NGX_DLSS_SR_OVERRIDE_RENDER_PRESET_SELECTION": "RENDER_PRESET_M",

    "DXVK_NVAPI_DRS_NGX_DLSS_FG_OVERRIDE_RENDER_PRESET_SELECTION": "RENDER_PRESET_C",

    "DXVK_NVAPI_DRS_SL_DLSS_OVERRIDE": "on",


    #By default, logs are saved to $HOME/steam-<STEAM_GAME_ID>.log, overwriting any previous log with that name.
    #Log directory can be overridden with $PROTON_LOG_DIR.

    #enable logging
    #"PROTON_LOG": "1",

    #custom Wine debug logging
    #"WINEDEBUG": "+timestamp,+pid,+tid,+seh,+unwind,+threadname,+debugstr,+loaddll,+mscoree",

    #DXVK debug logging
    #"DXVK_LOG_LEVEL": "info",

    #DXVK-NVAPI debug logging
    #"DXVK_NVAPI_LOG_LEVEL": "info",

    #vkd3d debug logging
    #"VKD3D_DEBUG": "warn",

    #vkd3d-shader debug logging
    #"VKD3D_SHADER_DEBUG": "fixme",

    #wine-mono debug logging (Wine's .NET replacement)
    #"WINE_MONO_TRACE": "E:System.NotImplementedException",
    #"MONO_LOG_LEVEL": "info",

    #xalia debug logging
    #"XALIA_DEBUG": "1",
    #"XALIA_DEBUG_INPUT": "1",

    #general purpose media logging
#    "GST_DEBUG": "4",
    #or, verbose converter logging (may impact playback performance):
#    "GST_DEBUG": "4,WINE:7,protonmediaconverter:7",
    #"GST_DEBUG_NO_COLOR": "1",

    #Enable DXVK's HUD
#    "DXVK_HUD": "devinfo,fps",

    #Use OpenGL-based wined3d for d3d11, d3d10, and d3d9 instead of Vulkan-based DXVK
#    "PROTON_USE_WINED3D": "1",

    #Disable d3d11 entirely
#    "PROTON_NO_D3D11": "1",

    #Disable eventfd-based in-process synchronization primitives
#    "PROTON_NO_ESYNC": "1",

    #Disable futex-based in-process synchronization primitives
#    "PROTON_NO_FSYNC": "1",
}
