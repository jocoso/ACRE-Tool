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

1. Read and break down the script to create a detailed props list.
2. Collaborate with the director, production designer, and art department to finalize prop requirements.
3. Attend production meetings and rehearsals.
4. Source props through purchasing, renting, or fabrication.
5. Manage the props budget and track expenses.
6. Supervise prop artisans, carpenters, and assistant prop managers.
7. Plan and assign labor and resources for prop acquisition and construction.
8. Provide stand-in items for early rehearsals.
9. Set up and manage props tables backstage.
10. Ensure actors have their props before going on stage.
11. Maintain prop continuity throughout the production.
12. Secure valuable props after each performance.
13. Coordinate the return of rented or borrowed items.
14. Organize prop storage between performances.
15. Manage the strike process for props at the end of the production.
16. Maintain an inventory of props and manage the props storage area.
17. Research historical accuracy of props for period productions.
18. Train actors on proper use of props when necessary.
19. Manage the transportation of props to and from the production site.
20. Organize the sale or disposal of props after the production ends.
21. Work with special effects and stunts departments for specific prop requirements.
22. Ensure props meet safety standards and regulations.
23. Maintain and repair props as needed throughout the production.
24. Create a "set and strike" schedule for props.
25. Coordinate with the set decorator to ensure cohesive visual aesthetics.
26. Oversee the creation of custom props when necessary.
27. Manage food styling for scenes involving food props.
28. Handle animals used as props (in some productions).
29. Maintain logical progression of props throughout the story (props breakdown).

---

## Stage Manager

The **Stage Manager** is responsible for the smooth operation of all activities on stage, serving as the main hub of communication between the director, actors, and technical crew.

### Responsibilities

1. Attend all rehearsals and performances.
2. Create and manage the master calendar for rehearsals, deadlines, and performances.
3. Coordinate auditions with the director.
4. Handle script distribution and collection.
5. Prepare cast and crew contact lists.
6. Tape out the set dimensions on the rehearsal floor.
7. Set up and clean the rehearsal and performance spaces.
8. Record the director's blocking and assist actors with it.
9. Take line notes and prompt actors when needed.
10. Manage rehearsal props and furniture.
11. Chair production meetings.
12. Develop preset lists and running order lists.
13. Organize backstage storage areas.
14. Write and distribute daily rehearsal, production meeting, and performance reports.
15. Facilitate communication between production staff, cast, and crew.
16. Record all technical cues in the prompt book.
17. Manage the production callboard.
18. Monitor actors' attendance and punctuality.
19. Coordinate technical and dress rehearsals.
20. Supervise technicians, deck hands, and board operators.
21. Organize and supervise special rehearsals (fight calls, dance combinations, etc.).
22. Call all cues during performances.
23. Create and maintain the prompt book (master copy of the script).
24. Work closely with the director during rehearsals.
25. Ensure the production runs smoothly and as the director intended.
26. Coordinate with designers and craftspeople.
27. Manage set changes and create furniture and prop plans.
28. Oversee the entire show during each performance.
29. Solve problems and answer questions for cast and crew.
30. Maintain safety protocols backstage.

---

PropManager is a class.

	##########################
	During its construction the PropManager:
		SETS a Table (null_objects_table) of GenericObjectType instances catalogued by the keyword `classname`, 
		a Table (inventory_table) of Objects prefabs catalogued by the keyword `prop_id`,
		and a Table (prop_continuity_table) containing two lists, catalogued by:
			`buffer_list`: a List of keywords `prop_id`,
			`cache_list`: a List of keywords `prop_id`.
	##########################

	##########################
	The function `nullify` takes a GenericObjectType type (object_class_arg) as a parameter, when executed it:
		DEFINES GenericObjectType instance (nullptr) TO Empty,
		VERIFIES if the classname has been added to the local Table (null_objects_table), if it has:
			SET GenericObjectType instance TO the instance of a null object located in local Table (null_object_table),
		HOWEVER, if the classname hasn't been added yet:
			SET the GenericObjectType (nullptr) TO an empty instance of a GenericObjectType,
			ADD the instance (nullptr), TO the local Table (null_objects_table),
		and finally RETURNS the GenericObjectType instance (nullptr).
			
	##########################

	##########################
    	The function `read_script` takes File object instace (script_file_arg) as a parameter; it then reads the script by:
    		VERIFYING the File Object instance (script_file_arg) is fit to use, and if it isn't the function will:
    			RAISE an error,
    			and EXIT the program urgently.

        	SETTING a List of Words (excerpt_list).
        
		#FOR each (line) in the script_file, the function:
			VERIFIES if the prop flag is set to true, because if it does the function will:
				a) VERIFY if the current line contains a token for creating a new prop, because if the line contains such token then the function:
					RAISES an error,
					and EXIT the program urgently;
				b) VERIFY if the current line contains a token for ending the creation of a new prop, because if the line contains such token then the function:
					SETS the prop flag to false,
					ADDS the new excerpt to excerpts_list,
					CLEANS the excerpt_list from all words,
					and CONTINUES to the next line;
				c) ONLY AFTER, the function will: 
					ADD the line to the excerpt_list,
					and CONTINUE to the next line;
					
		#For each (excerpt) in the excerpt_list, the function: 
			VERIFIES if the excerpt has all the data required to be turned into a prefab, and if it doesn't the function will:
				RAISE a warning,
				and CONTINUE to the next line;
			ONLY AFTER, the function will:
				FORMAT the data to resemble a prop prefab,
				ADD the prefab TO the local inventory. 
	##########################		
        
        ##########################
        The FUNCTION `generate_propbox` takes a Manager instance (manager_arg) as a parameter, it then generates a Propbox by:
        	DEFINING an instance of a Propbox (box) AS a New instance of a Propbox with the Manager instance (manager_arg) passed during construction;
        	
        	#FOR each List of Words (prop_prefab) in local Table (inventory_table):
        		DEFINE a Prop instance (tmp) AS a New instance of a Prop with the List of Words (prop_prefab) passed during construction,
        		ADD the Prop instance (tmp) TO the Propbox instance (box)
        	
        	Once all is done, it RETURNS the instance of a Propbox (box).
        ##########################
        

    def attend_meetings(self, PropToolbox, {additions}):
        """Modifies a toolbox without changing their blueprint."""
        # Asures PropToolbox is a healthy instance of the object before proceeding.
	# Makes a copy of the Toolbox.

	# 	If the instance is unhealthy, raises a Warning and returns an instance of nullify(PropToolbox)

	# Go through the list of additions:
	#	Generate addition (if needed)
	#	Integrate addition to toolbox
        
	# returns a changed toolbox. The lifecycle of this box lasts for as long as the intance exists and ceases existing inside this class after returned.
	return PropToolbox

    def source_props(self, {tags}, prefab_prop):
        """Creates and returns an instance of a prop following the Script tags and the prop prefab."""
        # If prefab_prop, instantiate an empty instance of type prefab_prop.
	#	Otherwise, instantiate an empty instance of type Prop

	# Traverse the list of tags, for each tag:
	#	Assign an appropriate spellScripts to the empty Prop.
        return Prop

    def manage_budget(self):
        """Debugger"""
        # TBD: Can work to determine efficient running. The `budget` will become synonymous with how well the framework executes.
        return TBD

    def supervise_artisans(self, prop):
        """Helper function to check if a prop's health. Returns True if the prop can be used in game."""
        # Verify prop is an intance of prop, if it is not:
	# 	Trigger InvalidClassError
	# Verify prop isn't empty, if it is:
	# 	Trigger EmptyPropWarning
	# Verify prop contains the SpellScript's required by tag, if it doesn't:
	#	Calls source_prop function with prop as argument.
        return Prop

    def plan_resources(self, actors, items, sets, set_states):
        """Update and Organizes assets inside the local inventory."""
        # Verify the inventory is empty, if it is not:
	#	Udates all the Props inside the local inventory.
	# Insert actors to local inventory.
	# Insert items to local inventory.
	# Insert set_states to local inventory.
        return None

    def provide_stand_in_items(self):
        """Returns a testing set."""
        # Call the local source_prop function with a 'testing' tag and a TestingSet class for arguments, however if there is an issue:
	#	Raise a BasicWarning,
	#	Call local nullify function with a Set class as argument.
        return Set

    def setup_props_table(self, previous_table, updated_table):
        """Adds props to the table at any point. The lifecycle of these props will lasts for as long as the save exists and will be resetted once a new game is started.
"""
        # Compare the tables,
	# Update what is the same,
	# Insert what is different only if the instace is healthy, if it is not:
	# 	Raise BasicError and exit.
        pass

    def ensure_actor_access(self, {Actor}, auth_level):
        """Changes the level of authorization for at least one instance of Author."""
        # Verify the list has at least one actor, if not:
	#	Raise BasicWarning,
	#	return nothing.

        # For each actor instance in the list:
	#	Update the instance auth_level
	return {Actor}

    def maintain_continuity(self, Prop):
        """Tracks the changes done to each prop and save the previous iteration. This prop function deletes the previous saved instance in the map and substitute it with the new iteration."""
	# Verify the prop id is in prop_continuity.basic, if it isnt:
	#	Verify the prop id is in prop_continuity.cache, if it is:
	#		Function assumes the screenwriter wants the prop back into the game and does so.
	#	However, if the prop is not in prop_continuity.cache:
	#		Raise PropNotFoundError and exit.
	
	# Verify the prop id is in prop_continuity.cache, if it isnt:
	# 	Insert the Prop instance located in prop_continuity.basic in prop_continuity.cache by using the prop_unique_id as key.
	# However, if the prop id is already in prop_continuity.cache:
	#	Replace the previous instance with the current instance located at prop_continuity.basic,
	#	Replace the variable containing the previous Prop instance for the new one.
        return self.prop_continuity.basic

    def secure_valuable_props(self, "script-excerpt"):
        """Used to instantiate system Props, if or when they are needed."""
        # While traversing the script-excerpt:
	#	Verify the excerpt can be turned into a Prop, if it can't:
	#		Raise UqualifiedSystemPropError and exit
	#	If the section can be turned into a Prop:
	#		Instantiate an empty Prop,
	#		Fill the Prop with the data required,
	#		Call source_props with the newly instantiate Prop as an argument.
        pass

    def coordinate_returns(self, prop_id_list):
        """Deletes a list of props from the inventory and prop_continuity.basic."""
        # Traverse each prop_id the prop_list:
	#	Verify if the prop_id is in the inventory, if yes:
	#		Delete the prop
	#	Verify if the prop_id is in the prop_continuity.basic, if yes:
	#		Delete the prop	
        #	Returns the instance of the Prop that was deleted.
	return Prop

    def organize_storage(self, previous_storage, updated_storage):
        """Update and save the inventory list to resemble the updated_storage."""
        # Create an empty list and label it name_storage.
	# Compare previous_storage with updated_storage, if item doesn't match:
	#	add item to new list.
	# however, if the item match:
	# 	update item,
	#	add the item to the new list.
        # Replace previous_storage with the new_storage.
	pass

    def manage_strike_process(self):
        """Reset the class by returning the  memory to the machine and killing the main loop."""
        # Validate the user wants to execute this function, if not:
	#	pass the execution.
	# Traverse each item in local variable:
	#	update item,
	#	save item,
	#	remove item from memory.
        pass

    def maintain_inventory(self):
        """Updates the inventory."""
        # Traverse each item in the local inventory:
	#	update the item.
        pass

    def research(self, "script_excerpt"):
        """Instantiates a generic Prop based on script excerpt argument."""
        # Instantiate a Prop with tags from the script.
	# Call supervise_prop with the new prop as an argument to add the SpellScript's.
	# returns the generic prop.
        return Prop

    def train_actors(self, actor_foo, ai_player_type):
        """Infuse an actor with AI."""
        # Verify the ai_player_type exists in the list of AI's, if it does:
	# 	Infuse the actor with the ai.
	# However, if it doesn't exist:
	#	Verify the screenwriter wants the program to use a generic ai, if they do:
	#		Infuse the action with a generic ai.
	# return the newly infused actor.
        return Actor

    def manage_transportation(self, requested_prop_id):
        """Manage the transportation of props from inside this class to other classes."""
        # Verify requested_prop is in the inventory, if it is:
	#	Verify requested_prop is in the list of instantiated objects, if it is:
	#		return the instance of the requested object.
	#	However, if it is not in instantiated object:
	#		Call local instantiate_prop with the prefab located in the inventory,
	#		Insert instance into the list of instantiated objects.
	# However, if the requested prop is not in the inventory:
	# Insert into inventory
	# return the newly created Prop
        return Prop


    def work_with_special_effects(self, script_excerpt):
        """Creates a special effect Prop from a script_excerpt"""
        # Analyze the Excerpt and Retrieve a list of prefabs from the excerpt.
        # Insert each prefab into the local inventory.
	pass

    def ensure_safety_standards(self):
        """Ensure props meet safety standards and regulations of the framework."""
        # Verify that for each item x, x is missing no components.
	# returns True if the condition above is met.
        return True

    def maintain_and_repair(self, prop_id):
        """Maintain and repair props as needed throughout the lifecycle."""
        # Verify if a prop exists with an id that matches prop_id, if one does:
	# 	Verify if there is a prefab is saved already in the local inventory, if one does:
	#		Retrieve the prefab,
	#		Turn it into a Prop,
	#		Replace the old instance with the newly created one.
	# 		Return the newly created instance.
        return Prop

    def create_sets(self, script_excerpt):
        """Returns an instance of Set object based on the excerpt."""
        # Validate that the excerpt can be turned into a Set, if it can not:
	# 	raise an error.

	# Creates an prefab based on the script_excerpt.
	# Pass it to the class to create a new Set.
	# Test for integrity errors.
	# Add the prefab to the inventory.
	# Return the newly created Set

        return Set

    def coordinate_with_set_decorator(self, Set, {decorations}):
        """Safetly applies decorations to a Set."""
        # Verify the integrity of the Set to check it's healthy, if it isn't:
	#	raise a warning.
	#	Verify the user wants to proceed, if they don't:
	#		exit gracefully.

	# Integrate decoration into the Set.
	# Return the Set.
        return Set

    def oversee_custom_props(self, script_excerpt or prefab):
        """Returns a Prop without adding them to the local inventory."""
        # Verify the excerpt will work as a prefab.
	# Turn the excerpt into a prefab.
	# Create an instance of the prefab.
	# Return the newly created instance.
	
        return Prop

    def manage_food_styling(self, script_excerpt):
        """Returns a consumable prop based on the excerpt."""
        # Verify the excerpt will work as a prefab.
        # Turn the excerpt into a prefab.
        # Create an instance of the prefab.
        # Return the newly created instance.
	
	return ConsumableProp
       
