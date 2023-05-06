// Get modal dialog's inner and outer <div/>
modal_div = document.querySelector(".modal");
modal_inner_div = document.querySelector(".modal-content");

// Get word-list containers <h5/>
adjectives_list_h5 = document.getElementById("adjectives");
nouns_list_h5 = document.getElementById("nouns");
verbs_list_h5 = document.getElementById("verbs");
miscellanies_list_h5 = document.getElementById("miscellanies");

// Turn off visibility of all <h5/>
word_lists_off = function() {
  adjectives_list_h5.style.display = "none";
  nouns_list_h5.style.display = "none";
  verbs_list_h5.style.display = "none";
  miscellanies_list_h5.style.display = "none";
}

// Set up regex for placeholder type detection
const regex_adjective = /^adjective-/;
const regex_noun = /^noun-/;
const regex_verb = /^verb-/;
const regex_miscellany = /^miscellany-/;

// Generic placeholder <span/> listeners
/* 
Iterate over each placeholder <span/> and assign callback to launch modal dialog.
*/
document.querySelectorAll('.underline').forEach(placeholder_span => {
  // deBuG: Regex working correctly as filter?
  if (regex_noun.test(placeholder_span.id)) {
    console.log("Noun:" + placeholder_span.id);
  }
  // Set callback on placeholder <span/> !!!
  placeholder_span.addEventListener('click', function() {
    // Turn off all <h5/> 
    word_lists_off();
    modal_div.style.display = "block";
    // Turn on the <h5/> according to trigger
    if (regex_adjective.test(placeholder_span.id)) {
     adjectives_list_h5.style.display = "inline"; 
    } else if (regex_noun.test(placeholder_span.id)) {
      nouns_list_h5.style.display = "inline";
    } else if (regex_verb.test(placeholder_span.id)) {
      verbs_list_h5.style.display = "inline";
    } else if (regex_miscellany.test(placeholder_span.id)) {
      miscellanies_list_h5.style.display = "inline";
    }
    // Stash triggering <span/> ID in <div/> for later 
    modal_inner_div.setAttribute("data-name", placeholder_span.id);
    
  })
}) 

// Generic word listeners
/*
Iterate over each word <span/> (source) in word-lists <h5/> and assign callback to insert inner HTML in triggering placeholder <span/> (target).
The target is communicated via data attr of modal inner <div/>.
*/
document.querySelectorAll('[class$="-words"]').forEach(source_span => {
    source_span.addEventListener('click', function() {
      target_span = document.querySelector('#'+modal_inner_div.getAttribute("data-name")) 
      console.log('target: '+target_span.id)
      target_span.innerHTML = source_span.innerHTML;
      modal_div.style.display = "none";
      
    });
});
                                              

