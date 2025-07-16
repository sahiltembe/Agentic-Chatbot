import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graphbuilder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_resultui import DisplayResultStreamlit


def load_langgraph_agentic_app():
    """
    Loads and runs the LangGraph AgenticAI Application with Streamlit UI.
    This function initializes the UI, handle user input, configure the LLM model
    sets up the graph based on the selected use case, and display the output while
    implementing exceptions handling for robustness. 
    """

    ## load ui
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error:Failed to load user input from the UI")
        return
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error:LLM model could not be initalized")
                return 
            
            usecase=user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No use case selected. ")

            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup as failed- {e}")
                return

        except Exception as e:
            st.error(f"Error: Graph set up failed -{e}")
            return

   