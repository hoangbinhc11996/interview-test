package com.interview.DOMs;
import org.springframework.data.annotation.Id;

public class EnglishVietnameseSentences {
    public EnglishVietnameseSentences(){}

    public EnglishVietnameseSentences(String text, String audio_url, Long translate_id, String translate_text){
        this.text = text;
        this.audio_url = audio_url;
        this.translate_id = translate_id;
        this.translate_text = translate_text;
    }

    @Id
    private  Long id;

    private  String text;

    private  String audio_url;

    private Long translate_id;

    private  String translate_text;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getAudio_url() {
        return audio_url;
    }

    public void setAudio_url(String audio_url) {
        this.audio_url = audio_url;
    }

    public String getTranslate_text() {
        return translate_text;
    }

    public void setTranslate_text(String translate_text) {
        this.translate_text = translate_text;
    }

    public Long getTranslate_id() {
        return translate_id;
    }

    public void setTranslate_id(Long translate_id) {
        this.translate_id = translate_id;
    }
}
