
from django.shortcuts import HttpResponse

def task_create(request):
    html_response = """
     <h1>Task create page</h1>
    <style>
    h1 {
        color:violet; 
        background-color:lavenderblush;
        text-align: center;
        padding: 10px;
        font-size: 36px;
    
    } 
    form {
        padding: 20px;
        border: 1px solid #ddd;
        background-color: #f9f9f9;
        width:300px;
        display: flex;
        flex-direction: column;
        width: 70%;
        
    }
    label {
        display: block;
        margin-bottom: 10px;
    }
    </style>
    
    <form>
    <label for=fname>
        Task name:
        <input type="text" placeholder="task name" id="fname" />
    </label>
    <br> <br>
    
    <label>Description:</label>
    <textarea></textarea>
    <br> <br>
    
    <label for="term">
        Deadline:
        <input type="Date">
    </label>
    <br> <br>
    
    <label>
        Important level:
        <select> 
            <option value="low">Low</option> 
            <option value="med">Medium</option> 
            <option value="high">High</option> 
        </select>
    </label>
    <br> <br>
    
    <button type="submit">Save the task</button>
    </form>
    
    """
    return HttpResponse(html_response)