set(hdrs PenKobu.h
    PARENT_SCOPE
    emergencySVC_impl.h
    )

install(FILES ${hdrs} DESTINATION ${INC_INSTALL_DIR}/${PROJECT_NAME_LOWER}
    COMPONENT library)

