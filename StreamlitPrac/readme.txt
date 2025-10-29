installation:
    -pip install streamlit
    -streamlit hello
START:
- open cmd promt- type python
                -exit()
- pip install streamlit
- create ex.py

RUN:
    checkpoint1: pythone file folder should activate in cmd promt.
                - if not change dir to that folder.
    checkpoint2: normal pythone file with run: <file_name>.py
                                            - ex1.py
                                            - if prompted enter your email id and allow.
    streamlit python files will run :
                                    python -m streamlit run <file_name>.py
                                    python -m streamlit run ex1.py

    Streamlit emoji shortcodes:
    https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/


same can be done in Anaconda prompt:
    - pip install streamlit
    - go to dirrectory.
    - python -m streamlit run example.py



(variable) def write(
    *args: Any,
    unsafe_allow_html: bool = False
) -> None
Displays arguments in the app.

This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, st.write() has some unique properties:

You can pass in multiple arguments, all of which will be displayed.
Its behavior depends on the input type(s).
Parameters
*args : any
One or many objects to display in the app.

Each type of argument is handled as follows: header-rows : 1

Type
Handling
str
Uses st.markdown().
dataframe-like, dict, or list
Uses st.dataframe().
Exception
Uses st.exception().
function, module, or class
Uses st.help().
DeltaGenerator
Uses st.help().
Altair chart
Uses st.altair_chart().
Bokeh figure
Uses st.bokeh_chart().
Graphviz graph
Uses st.graphviz_chart().
Keras model
Converts model and uses st.graphviz_chart().
Matplotlib figure
Uses st.pyplot().
Plotly figure
Uses st.plotly_chart().
PIL.Image
Uses st.image().
generator or stream (like openai.Stream)
Uses st.write_stream().
SymPy expression
Uses st.latex().
An object with ._repr_html()
Uses st.html().
Database cursor
Displays DB API 2.0 cursor results in a table.
Any
Displays str(arg) as inline code.