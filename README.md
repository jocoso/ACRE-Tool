# Active Reading Tool (ACRE Tool)

The **Active Reading Tool (ACRE Tool)** is a program designed to enhance engagement in reading by creating a unique interactive experience that resembles the interactivity of a video game, all within the format of a book.

## Requirements

For the ACRE Tool to function, it requires a **screenplay**. A screenplay is a `.screen` file written in Screen Language, which the ACRE engine executes. The program utilizes an architecture similar to how theater organizes its productions to execute the screenplay, involving:

- **A) Stage Manager**: Responsible for managing the intangible aspects (the story).
- **B) Props Manager**: Responsible for managing the tangible aspects (stage props, actors, sets, etc.).

---

## Prop Manager

The **Prop Manager** is responsible for all prop-related tasks, including the windows the user interacts with.

### Responsibilities

1. **Read and break down the script** to create a detailed props list.
2. **Collaborate with the director, production designer, and art department** to finalize prop requirements.
3. **Attend production meetings and rehearsals**.
4. **Source props** through purchasing, renting, or fabrication.
5. **Manage the props budget** and track expenses.
6. **Supervise prop artisans, carpenters, and assistant prop managers**.
7. **Plan and assign labor and resources** for prop acquisition and construction.
8. **Provide stand-in items for early rehearsals**.
9. **Set up and manage props tables backstage**.
10. **Ensure actors have their props** before going on stage.
11. **Maintain prop continuity** throughout the production.
12. **Secure valuable props** after each performance.
13. **Coordinate the return of rented or borrowed items**.
14. **Organize prop storage** between performances.
15. **Manage the strike process for props** at the end of the production.
16. **Maintain an inventory of props** and manage the props storage area.
17. **Research historical accuracy of props** for period productions.
18. **Train actors on proper use of props** when necessary.
19. **Manage the transportation of props** to and from the production site.
20. **Organize the sale or disposal of props** after the production ends.
21. **Work with special effects and stunts departments** for specific prop requirements.
22. **Ensure props meet safety standards and regulations**.
23. **Maintain and repair props** as needed throughout the production.
24. **Create a "set and strike" schedule for props**.
25. **Coordinate with the set decorator** to ensure cohesive visual aesthetics.
26. **Oversee the creation of custom props** when necessary.
27. **Manage food styling** for scenes involving food props.
28. **Handle animals used as props** (in some productions).
29. **Maintain logical progression of props** throughout the story (props breakdown).

---

## Stage Manager

The **Stage Manager** is responsible for the smooth operation of all activities on stage, serving as the main hub of communication between the director, actors, and technical crew.

### Responsibilities

1. **Attend all rehearsals and performances**.
2. **Create and manage the master calendar** for rehearsals, deadlines, and performances.
3. **Coordinate auditions** with the director.
4. **Handle script distribution and collection**.
5. **Prepare cast and crew contact lists**.
6. **Tape out the set dimensions** on the rehearsal floor.
7. **Set up and clean the rehearsal and performance spaces**.
8. **Record the director's blocking** and assist actors with it.
9. **Take line notes** and prompt actors when needed.
10. **Manage rehearsal props and furniture**.
11. **Chair production meetings**.
12. **Develop preset lists and running order lists**.
13. **Organize backstage storage areas**.
14. **Write and distribute daily rehearsal, production meeting, and performance reports**.
15. **Facilitate communication between production staff, cast, and crew**.
16. **Record all technical cues** in the prompt book.
17. **Manage the production callboard**.
18. **Monitor actors' attendance and punctuality**.
19. **Coordinate technical and dress rehearsals**.
20. **Supervise technicians, deck hands, and board operators**.
21. **Organize and supervise special rehearsals** (fight calls, dance combinations, etc.).
22. **Call all cues** during performances.
23. **Create and maintain the prompt book** (master copy of the script).
24. **Work closely with the director** during rehearsals.
25. **Ensure the production runs smoothly** and as the director intended.
26. **Coordinate with designers and craftspeople**.
27. **Manage set changes** and create furniture and prop plans.
28. **Oversee the entire show** during each performance.
29. **Solve problems and answer questions** for cast and crew.
30. **Maintain safety protocols backstage**.

---

## UDM for PropManager

```python
class PropManager:
    def __init__(self):
        # List of all the game prop data obtained from the script.
        self.props_list = []
        # Budget and expenses (currently not in use but kept for future needs).
        self.budget = 0.0
        self.expenses = 0.0
        # All instances of props.
        self.inventory = {}
        # Props that come with the library by default, used mostly for testing.
        self.prop_continuity = {}

    def read_script(self, script):
        """Read and break down the script to create a detailed props list."""
        # Implementation to parse the script and create a props list
        pass

    def finalize_requirements(self, director, production_designer, art_department):
        """Collaborate with the director, production designer, and art department to finalize prop requirements."""
        # Implementation for collaboration
        return False

    def attend_meetings(self):
        """Attend production meetings and rehearsals."""
        # Implementation for attending meetings
        pass

    def source_props(self, method, prop_details):
        """Source props through purchasing, renting, or fabrication."""
        # Implementation for sourcing props
        return None

    def manage_budget(self):
        """Manage the props budget and track expenses."""
        # TBD: Can work to determine efficient running. The `budget` will become synonymous with either space or time complexity.
        pass

    def supervise_artisans(self, prop):
        """Supervise prop artisans, carpenters, and assistant prop managers."""
        # Implementation for supervision
        pass

    def plan_resources(self):
        """Plan and assign labor and resources for prop acquisition and construction."""
        # Implementation for planning resources
        return None

    def provide_stand_in_items(self):
        """Provide stand-in items for early rehearsals."""
        # Implementation for providing stand-in items
        pass

    def setup_props_table(self):
        """Set up and manage props tables backstage."""
        # Implementation for setting up props tables
        pass

    def ensure_actor_access(self, character):
        """Ensure actors have their props before going on stage."""
        # Implementation for ensuring actors have props
        return None

    def maintain_continuity(self):
        """Maintain prop continuity throughout the production."""
        # Implementation for maintaining continuity
        return self.prop_continuity

    def secure_valuable_props(self):
        """Secure valuable props after each performance."""
        # Implementation for securing props
        pass

    def coordinate_returns(self, prop_list):
        """Coordinate the return of rented or borrowed items."""
        # Implementation for coordinating returns
        pass

    def organize_storage(self):
        """Organize prop storage between performances."""
        # Implementation for organizing storage
        return ""

    def manage_strike_process(self):
        """Manage the strike process for props at the end of the production."""
        # Implementation for managing the strike process
        pass

    def maintain_inventory(self):
        """Maintain an inventory of props and manage the props storage area."""
        # Implementation for maintaining inventory
        pass

    def research(self, prop, script):
        """Research historical accuracy of props for period productions."""
        # Implementation for research
        pass

    def train_actors(self, actor_foo, ai_player_type):
        """Train actors on proper use of props when necessary."""
        # Implementation for training actors
        pass

    def manage_transportation(self, requested_prop):
        """Manage the transportation of props to and from the production site."""
        # Implementation for managing transportation
        return None

    def organize_sale_or_disposal(self):
        """Organize the sale or disposal of props after the production ends."""
        # Implementation for organizing sale or disposal
        pass

    def work_with_special_effects(self):
        """Work with special effects and stunts departments for specific prop requirements."""
        # Implementation for collaboration with special effects
        pass

    def ensure_safety_standards(self):
        """Ensure props meet safety standards and regulations."""
        # Implementation for ensuring safety standards
        pass

    def maintain_and_repair(self):
        """Maintain and repair props as needed throughout the production."""
        # Implementation for maintenance and repair
        pass

    def create_sets(self, script):
        """Creates the sets."""
        # Implementation for creating sets
        pass

    def coordinate_with_set_decorator(self, set):
        """Coordinate with the set decorator to ensure cohesive visual aesthetics."""
        # Implementation for coordination
        pass

    def oversee_custom_props(self):
        """Oversee the creation of custom props when necessary."""
        # Implementation for overseeing custom props
        pass

    def manage_food_styling(self):
        """Manage food styling for scenes involving food props."""
        # Implementation for food styling
        pass

