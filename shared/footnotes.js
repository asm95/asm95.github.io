$(document).ready(function(){
        // pwa.text_html.richtext.footnotes
        var sec_idx = 1;
        $('div.sec').each(function(){ // ignored index arg
                var $e = $(this);
                var $ref_c = $('<div style="margin-top:1em; font-size: 10pt;"></div>'); // references container
                var ref_idx = 1;
                $e.find('sup.fn').each(function(){
                        var $f = $(this);
                        var text = $f.html();
                        var ref_text = '[' +ref_idx+ ']';
                        var elem_id = 'sec' +sec_idx+ '_ref' + ref_idx;
                        $f.html('<a href="#'+elem_id+'">' +ref_text+ '</a>');
                        $ref_c.append('<p id="'+elem_id+'">' +ref_text+ ' ' +text+ '</p>'); 
                        ref_idx++;
                });
                $($e).append($ref_c);
                sec_idx++;
        });
});