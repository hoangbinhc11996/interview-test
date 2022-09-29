package com.interview.Controllers;

import com.interview.DOMs.EnglishVietnameseSentences;
import com.interview.Repositories.SentenceRepository;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/")
public class SentenceController {

    private final SentenceRepository sentenceRepository;

    public SentenceController(SentenceRepository sentenceRepository) {
        this.sentenceRepository = sentenceRepository;
    }

    @PostMapping("/api/sentences")
    @ResponseStatus(HttpStatus.CREATED)
    public EnglishVietnameseSentences createSentence(@RequestBody EnglishVietnameseSentences sentence) {
        return sentenceRepository.save(sentence);
    }

    @GetMapping("/api/allsentences")
    public Iterable<EnglishVietnameseSentences> getSentences() {
        return sentenceRepository.findAll();
    }

    @GetMapping(value = "/api/sentences")
    public Iterable<EnglishVietnameseSentences> getSentencesWithPaging(@RequestParam(defaultValue = "0") int page,
                                                                       @RequestParam(defaultValue = "10") int size) {
        Pageable pagingSort = PageRequest.of(page, size);
        return sentenceRepository.findAll(pagingSort);
    }
}