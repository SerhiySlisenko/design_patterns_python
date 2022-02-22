from behavioral.hw_jira_workflow.jira import Jira
from behavioral.hw_jira_workflow.jira_context import JiraContext


def main() -> None:
    """
    Client app
    """
    key_menu: str = ""
    jira_context: JiraContext = JiraContext(Jira("WPP-111", "Junior"))
    menu_actions = {
        "1": jira_context.start_work_on_jira,
        "2": jira_context.stop_work_on_jira,
        "3": jira_context.resolve_jira,
        "4": jira_context.reopen_jira,
        "5": jira_context.verify_jira,
        "6": jira_context.close_jira,
        "7": jira_context.change_assignee,
        "8": jira_context.print_jira,
    }

    while key_menu != "Q":
        print("\n   1 - Start Progress on JIRA" + "   2 - Stop Progress on JIRA   ")
        print("   3 - Resolve JIRA      " + "       4 - Reopen JIRA    ")
        print("   5 - Verify JIRA       " + "       6 - Close JIRA     ")
        print("   7 - Change assignee" + "          8 - Print JIRA details")
        print("   Q - exit")
        print("\n   Please, select menu point.")

        key_menu = str(input()).upper()
        if (action := menu_actions.get(key_menu)) is not None:
            if action == jira_context.change_assignee:
                assignee_name = input("Enter assignee name (e.g. Junior, Middle, Senior, Manager): ")
                action(assignee_name)
            else:
                action()


if __name__ == '__main__':
    main()
