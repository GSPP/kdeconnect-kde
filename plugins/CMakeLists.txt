include_directories(${CMAKE_SOURCE_DIR} ${CMAKE_BINARY_DIR}/core)
add_definitions(-DTRANSLATION_DOMAIN=\"kdeconnect-plugins\")
install(FILES kdeconnect_plugin.desktop DESTINATION ${SERVICETYPES_INSTALL_DIR})

add_subdirectory(ping)
add_subdirectory(battery)
add_subdirectory(remotecommands)
add_subdirectory(remotecontrol)
add_subdirectory(remotesystemvolume)
add_subdirectory(clipboard)
add_subdirectory(runcommand)

if(NOT APPLE)
add_subdirectory(presenter)
endif()

if(NOT SAILFISHOS)
    add_subdirectory(sendnotifications)
    add_subdirectory(mpriscontrol)
    add_subdirectory(photo)
    add_subdirectory(mprisremote)
    add_subdirectory(lockdevice)
    add_subdirectory(contacts)
    add_subdirectory(share)
    add_subdirectory(remotekeyboard)
    add_subdirectory(notifications)
    add_subdirectory(findmyphone)
    add_subdirectory(telephony)
    add_subdirectory(mousepad)
    add_subdirectory(sms)
    add_subdirectory(screensaver-inhibit)

    if(NOT APPLE)
        add_subdirectory(sftp)
    endif()

    if(KF5PulseAudioQt_FOUND OR WIN32)
        add_subdirectory(pausemusic)
    endif()

    if(Qt5Multimedia_FOUND AND (KF5PulseAudioQt_FOUND OR WIN32))
        add_subdirectory(findthisdevice)
    endif()

    if (WIN32 OR APPLE OR KF5PulseAudioQt_FOUND)
        add_subdirectory(systemvolume)
    endif()
endif()


# If we split notifications per plugin, in several notifyrc files, they won't
# appear in the same group in the Notifications KCM
install(FILES kdeconnect.notifyrc DESTINATION ${KNOTIFYRC_INSTALL_DIR})
