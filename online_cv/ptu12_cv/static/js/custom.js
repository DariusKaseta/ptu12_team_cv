$(document).ready(function() {
    $(document).on('click', '#add-education-form', function() {
    var lastEducationForm = $('.education-form:last');
    var newEducationForm = lastEducationForm.clone();

    newEducationForm.find('input').val('');
    newEducationForm.find('select').val('');
    
    
    var newIndex = $('.education-form').length;
      
    newEducationForm.find('input, select').each(function() {
    var name = $(this).attr('name');
        if (name) {
          
        $(this).attr('name', name.replace(/education-\d+/, 'education-form' + newIndex));
    }
    });
    
    $('#education-form-container').append(newEducationForm);
    return false;
});


$(document).on('click', '#add-work-experience-form', function() {
    var lastWorkExperienceForm = $('.work-experience-form:last');
    var newWorkExperienceForm = lastWorkExperienceForm.clone();
  
    newWorkExperienceForm.find('input').val('');
    newWorkExperienceForm.find('select').val('');
    
    
    var newPrefix = 'work-experience-' + ($('.work-experience-form').length + 1);
    newWorkExperienceForm.find('input, select').each(function() {
        var name = $(this).attr('name');
        if (name) {
        
        $(this).attr('name', name.replace('work_experience-0', newPrefix));
        }
    });
  
    $('#work-experience-form-container').append(newWorkExperienceForm);
    return false;
});


$(document).on('click', '#add-skill-form', function() {
    var lastSkillForm = $('.skill-form:last');
    var newSkillForm = lastSkillForm.clone();
  
    newSkillForm.find('input').val('');
    newSkillForm.find('select').val('');
    
    
    var newPrefix = 'skill-' + ($('.skill-form').length + 1);
    newSkillForm.find('input, select').each(function() {
    var name = $(this).attr('name');
    if (name) {
        
        $(this).attr('name', name.replace('skill-0', newPrefix));
        }   
    });
  
    $('#skill-form-container').append(newSkillForm);
    return false;
    });
});
