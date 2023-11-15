"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        rx.hstack(
            rx.skeleton(height="30px", width="120px", speed=1.5),
            rx.spacer(),
            rx.skeleton(height="30px", width="100px", speed=1.5),
            rx.skeleton(height="30px", width="100px", speed=1.5),
            rx.skeleton(height="30px", width="100px", speed=1.5),
            rx.button(rx.skeleton(height="15px", width="50px", speed=1.5),),

            padding_x="10",
            padding_y="5",
            
        ),
        
        
        rx.center(
            
            rx.vstack(
            rx.spacer(),
            rx.skeleton(height="30px", width="40%", speed=1.5),
            rx.box(width="40%", height="10px", bg="#d3d3d3"),
            rx.box(width="40%", height="50px", bg="transparent"),
            rx.flex(
                rx.input(
                height="60px",
                width="80%",
                bg="white",
            ),
                    rx.box(width="20%", height="60px", bg="#d3d3d3"),
            width="60%"),
            rx.spacer(),
            width="100%",
            height="600px",
            bg="#5D6D7E"            
        ),
            
        ),


        rx.vstack(
            rx.box(width="40%", height="20px", bg="transparent"),
            rx.skeleton(height="25px", width="200px", border_radius="10px", speed=1.5),
            rx.box(width="40%", height="100px", bg="transparent"),
            rx.flex(
                rx.spacer(),
              rx.box(
                rx.vstack(
                    rx.skeleton(height="150px", width="150px", border_radius="50%", speed=1.5),
                    rx.box(width="40%", height="20px", bg="transparent"),
                    rx.skeleton(height="20px", width="200px", speed=1.5),
                    rx.skeleton(height="10px", width="250px", speed=1.5),
                    rx.skeleton(height="10px", width="200px", speed=1.5),

                )
            ),
            rx.spacer(),
            rx.box(
                rx.vstack(
                    rx.skeleton(height="150px", width="150px", border_radius="50%", speed=1.5),
                    rx.box(width="40%", height="20px", bg="transparent"),
                    rx.skeleton(height="20px", width="200px", speed=1.5),
                    rx.skeleton(height="10px", width="250px", speed=1.5),
                    rx.skeleton(height="10px", width="200px", speed=1.5),

                )
            ),
            rx.spacer(),
            rx.box(
                rx.vstack(
                    rx.skeleton(height="150px", width="150px", border_radius="50%", speed=1.5),
                    rx.box(width="40%", height="20px", bg="transparent"),
                    rx.skeleton(height="20px", width="200px", speed=1.5),
                    rx.skeleton(height="10px", width="250px", speed=1.5),
                    rx.skeleton(height="10px", width="200px", speed=1.5),

                )
            ),
            rx.spacer(),
            
            width="100%"  
            ),           
        width="100%",
        height="600px"),

        rx.vstack(
            rx.skeleton(height="25px", width="200px", border_radius="10px", speed=1.5),
            rx.box(width="40%", height="100px", bg="transparent"),
            rx.grid(
                rx.grid_item(
                    rx.flex(
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.skeleton(height="75px", width="75px", border_radius="50%", speed=1.5),
                                ),
                                
                                rx.box(
                                    rx.vstack(
                                            rx.box(
                                                rx.skeleton(height="25px", width="220px", speed=1.5, padding_y="5px"),
                                                    rx.vstack(                               
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5,),
                                                        padding_y="15px"
                                                        ),
                                            margin_left="15px")
                                    
                                    ),
                                ),
                            ),
                        margin="auto"
                        ),
                    ),
                    col_span=3),
                rx.grid_item(
                    rx.flex(
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.skeleton(height="75px", width="75px", border_radius="50%", speed=1.5),
                                ),
                                
                                rx.box(
                                    rx.vstack(
                                            rx.box(
                                                rx.skeleton(height="25px", width="220px", speed=1.5, padding_y="5px"),
                                                    rx.vstack(                               
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5,),
                                                        padding_y="15px"
                                                        ),
                                            margin_left="15px")
                                    
                                    ),
                                ),
                            ),
                        margin="0"
                        ),
                    ),
                    col_span=3),
                    rx.grid_item(
                    rx.flex(
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.skeleton(height="75px", width="75px", border_radius="50%", speed=1.5),
                                ),
                                
                                rx.box(
                                    rx.vstack(
                                            rx.box(
                                                rx.skeleton(height="25px", width="220px", speed=1.5, padding_y="5px"),
                                                    rx.vstack(                               
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5,),
                                                        padding_y="15px"
                                                        ),
                                            margin_left="15px")
                                    
                                    ),
                                ),
                            ),
                        margin="auto"
                        ),
                    ),
                    col_span=3),
                rx.grid_item(
                    rx.flex(
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.skeleton(height="75px", width="75px", border_radius="50%", speed=1.5),
                                ),
                                
                                rx.box(
                                    rx.vstack(
                                            rx.box(
                                                rx.skeleton(height="25px", width="220px", speed=1.5, padding_y="5px"),
                                                    rx.vstack(                               
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5,),
                                                        padding_y="15px"
                                                        ),
                                            margin_left="15px")
                                    
                                    ),
                                ),
                            ),
                        margin="0"
                        ),
                    ),
                    col_span=3),
                    rx.grid_item(
                    rx.flex(
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.skeleton(height="75px", width="75px", border_radius="50%", speed=1.5),
                                ),
                                
                                rx.box(
                                    rx.vstack(
                                            rx.box(
                                                rx.skeleton(height="25px", width="220px", speed=1.5, padding_y="5px"),
                                                    rx.vstack(                               
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5,),
                                                        padding_y="15px"
                                                        ),
                                            margin_left="15px")
                                    
                                    ),
                                ),
                            ),
                        margin="auto"
                        ),
                    ),
                    col_span=3),
                rx.grid_item(
                    rx.flex(
                        rx.box(
                            rx.flex(
                                rx.box(
                                    rx.skeleton(height="75px", width="75px", border_radius="50%", speed=1.5),
                                ),
                                
                                rx.box(
                                    rx.vstack(
                                            rx.box(
                                                rx.skeleton(height="25px", width="220px", speed=1.5, padding_y="5px"),
                                                    rx.vstack(                               
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5),
                                                        rx.skeleton(height="10px", width="270px", speed=1.5,),
                                                        padding_y="15px"
                                                        ),
                                            margin_left="15px")
                                    
                                    ),
                                ),
                            ),
                        margin="0"
                        ),
                    ),
                    col_span=3),
                template_rows="repeat(2, 1fr)",
                template_columns="repeat(6, 1fr)",
                h="200px",
                width="100%",
                gap=4,
            ),

          
        height="500px"),
    
        rx.vstack(
            rx.box(width="40%", height="100px", bg="transparent"),
            rx.skeleton(height="25px", width="200px", border_radius="10px", speed=1.5),
            rx.box(width="40%", height="100px", bg="transparent"),

            rx.skeleton(height="20px", width="50%", speed=1.5, border_radius="md"),
            rx.skeleton(height="20px", width="85%", speed=1.5, border_radius="md"),
            rx.skeleton(height="20px", width="85%", speed=1.5, border_radius="md"),
            rx.skeleton(height="20px", width="30%", speed=1.5, border_radius="md"),
            rx.box(height="20px", width="20%", bg="transparent"),
            rx.skeleton(height="8px", width="20%", speed=1.5, border_radius="md"),
            rx.skeleton(height="8px", width="10%", speed=1.5, border_radius="md"),

            rx.box(height="50px", width="20%", bg="transparent"),
            
                rx.hstack(
                    rx.spacer(),
                    rx.skeleton(height="100px", width="100px", border_radius="50%", speed=1.5),
                    rx.spacer(),
                    rx.skeleton(height="100px", width="100px", border_radius="50%", speed=1.5),
                    rx.spacer(),
                    rx.skeleton(height="100px", width="100px", border_radius="50%", speed=1.5),
                    rx.spacer(),
                width="100%"),
        width="100%",
        height="700px"),
    
        rx.vstack(
            rx.box(width="40%", height="10px", bg="transparent"),

            rx.hstack(
                rx.skeleton(height="10px", width="70px", speed=1.5, border_radius="md", padding_x="5px"),
                rx.skeleton(height="10px", width="70px", speed=1.5, border_radius="md", padding_x="5px"),
                rx.skeleton(height="10px", width="70px", speed=1.5, border_radius="md", padding_x="5px"),
            ),
            rx.skeleton(height="10px", width="10%", speed=1.5, border_radius="md"),
        bg="#d3d3d3",
        width="100%",
        height="100px"),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
